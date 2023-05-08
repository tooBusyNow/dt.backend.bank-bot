import logging
from functools import wraps

from telegram import Update
from telegram.ext import ContextTypes

from app.internal.api_v1.telegram_messages import ME_WITH_NO_USER, NO_VERIFIED_PN

from app.internal.api_v1.users.db.repositories import UserRepository
from app.internal.api_v1.users.domain.services import UserService

logger = logging.getLogger("django.server")


def verified_phone_required(func):
    """
    This decorator function restricts access to all other Telegram commands
    (except /start, /set_phone and /help) unless user has a verified phone number.
    ----------
    :param func: some function that acts like a command handler
    """

    user_repo = UserRepository()
    user_services = UserService(user_repo=user_repo)

    @wraps(func)
    async def wrapper(_self, update : Update, context : ContextTypes.DEFAULT_TYPE):
        user_phone_number = await user_services.get_user_field_by_id(
            tlg_id=update.effective_user.id, field_name="phone_number"
        )

        if user_phone_number:
            await func(_self, update, context)
        else:
            logger.info(f"User with {update.effective_user.id} ID don't have access to this function: {func.__name__}")
            await context.bot.send_message(chat_id=update.effective_chat.id, text=NO_VERIFIED_PN)

    return wrapper
