import logging

from phonenumber_field.phonenumber import PhoneNumber
from phonenumbers.phonenumberutil import NumberParseException

from app.internal.models.user import User
from app.internal.services.telegram_service import verified_phone_required
from app.internal.services.user_service import get_user_from_db, save_user_to_db, update_user_phone_number

from app.internal.services.payment_service import get_card_from_db, get_account_from_db

from .telegram_messages import (
    ABSENT_PN_MSG,
    ABSENT_ID_NUMBER,
    HELP_MSG,
    INVALID_PN_MSG,
    NOT_INT_FORMAT_MSG,
    get_success_phone_msg,
    get_unique_start_msg,
)

logger = logging.getLogger("django.server")


async def start(update, context):
    """
    Handler for /start command.
    (Handlers usually take 2 arguments: update and context).
    ----------
    :param update: recieved Update object
    :param context: context object passed to the callback

    """
    user_data = update.effective_user
    chat_id = update.effective_chat.id

    tlg_user = User(
        tlg_id=user_data.id,
        username=user_data.username,
        first_name=user_data.first_name,
        last_name=user_data.last_name if user_data.last_name else "",
        phone_number="",
    )

    await save_user_to_db(tlg_user)
    await context.bot.send_message(chat_id=chat_id, text=get_unique_start_msg(user_data.username))


async def get_help(update, context):
    """
    Handler for /help command.
    Returns some info about currently supported commands.
    ----------
    :param update: recieved Update object
    :param context: context object passed to the callback
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG)


async def set_phone(update, context):
    """
    Handler for /set_phone command.
    Supports phone validation and user existence checking.
    ----------
    :param update: recieved Update object
    :param context: context object passed to the callback
    """
    user_data = update.effective_user
    chat_id = update.effective_chat.id
    command_data = update.message.text.split(" ")

    if len(command_data) == 2:
        user_from_db = await get_user_from_db(user_data.id)
        phone_number = command_data[1]

        if phone_number.startswith("+"):
            try:
                parsed_number = PhoneNumber.from_string(phone_number)

                await update_user_phone_number(user_from_db, parsed_number)
                await context.bot.send_message(chat_id=chat_id, text=get_success_phone_msg(parsed_number))

            except NumberParseException:
                logger.info("User did not provide a valid phone number")
                await context.bot.send_message(chat_id=chat_id, text=INVALID_PN_MSG)
            finally:
                return

        await context.bot.send_message(chat_id=chat_id, text=NOT_INT_FORMAT_MSG)
        return
    await context.bot.send_message(chat_id=chat_id, text=ABSENT_PN_MSG)


@verified_phone_required
async def me(update, context):
    """
    Hander for /me command.
    Returns full information about Telegram user.
    ----------
    :param update: recieved Update object
    :param context: context object passed to the callback
    """
    user_id = update.effective_user.id
    user_from_db = await get_user_from_db(user_id)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Here is some info about you:\n\n" f"{str(user_from_db)}"
    )

@verified_phone_required
async def check_payable(update, context):
    """
    Handler for /check_card command
    Returns remaining value on specified card or 
    error message if card is absent. 
    ----------
    :param update: recieved Update object
    :param context: context object passed to the callback
    """
    chat_id = update.effective_chat.id
    command_data = update.message.text.split(" ")

    if len(command_data) == 2:
        obj_option = None
        uniq_id = str(command_data[1])

        if command_data[0] == '/check_card':
            obj_option = await get_card_from_db(uniq_id)
        else:
            obj_option = await get_account_from_db(uniq_id)

        if obj_option:
            await context.bot.send_message (
            chat_id=update.effective_chat.id, text=f"This card / account balance is {obj_option.value}"
        )
        else:
            logger.info(f'Card / account with ID {uniq_id} not found in DB')
            await context.bot.send_message (
            chat_id=update.effective_chat.id, text=f"Unable to find balance for this card / account"
        )
        return
                
    await context.bot.send_message(chat_id=chat_id, text=ABSENT_ID_NUMBER)

    