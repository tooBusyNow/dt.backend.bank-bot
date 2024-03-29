import logging

from django.conf import settings
from prometheus_client import start_http_server
from telegram.ext import AIORateLimiter, Application, ApplicationBuilder

from app.internal.api_v1.favourites.bot import register_telegram_favourite_handlers
from app.internal.api_v1.payment.bot import register_telegram_payment_handlers
from app.internal.api_v1.users.bot import register_telegram_user_handlers

from .ngrok_parser import parse_ngrok_url

logger = logging.getLogger("stdout_with_tlg")


def get_bot_application() -> Application:
    """
    This function creates default
    Telegram Bot Application and sets up
    command handlers.
    :return: Bot Application instance
    """
    application = ApplicationBuilder().token(settings.TLG_TOKEN).rate_limiter(AIORateLimiter()).build()

    setup_application_handlers(application)

    return application


def start_metrics_endpoint():
    """
    Starts endpoint for metrics collection.
    """
    start_http_server(settings.METRICS_PORT)


def start_polling_bot():
    """
    Starts a new instanse of Telegram Bot
    Application in polling mode
    """
    application: Application = get_bot_application()
    start_metrics_endpoint()

    logger.info("Started")
    application.run_polling()


def start_webhook_bot():
    """
    Sets a webhook to recieve incoming Telegram updates.
    Tries to use WEBHOOK_URL from .env file.

    If we don't have an available IP in global net, we have to
    use Ngrok as a Proxy to recieve HTTPS POST requests from Telegram.
    ----------
    :param application: Bot Application instance
    """

    application: Application = get_bot_application()
    start_metrics_endpoint()

    url = settings.WEBHOOK_URL
    if not url:
        url = parse_ngrok_url()

    logger.info("Started")
    application.run_webhook(
        listen="0.0.0.0",
        port=settings.WEBHOOK_PORT,
        url_path="webhook",
        webhook_url=f"{url}",
        close_loop=False,
        drop_pending_updates=True,
    )


def setup_application_handlers(application: Application):
    """
    Creates command handlers for specified Bot Application.
    Each handler represents a single Telegram command.
    ----------
    :param application: Bot Application instance
    """

    register_telegram_user_handlers(application)
    register_telegram_favourite_handlers(application)
    register_telegram_payment_handlers(application)
