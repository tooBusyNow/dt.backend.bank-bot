import logging

from django.core.management.base import BaseCommand

from app.internal.bot import start_polling_bot

logger = logging.getLogger("stdout_with_tlg")


class Command(BaseCommand):
    help = "Starts Telegram Bot Application in polling mode"

    def handle(self, *args, **options):
        logger.info("Starting...")
        start_polling_bot()
