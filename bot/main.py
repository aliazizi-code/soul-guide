import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from bot.handlers import get_handlers
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()

    for handler in get_handlers():
        app.add_handler(handler)

    logger.info("ربات هارلی شروع به کار کرد...")
    app.run_polling()

if __name__ == "__main__":
    main()
