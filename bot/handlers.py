from telegram.ext import CommandHandler, MessageHandler, filters
from bot.session import start_chat, end_chat, handle_message

def get_handlers():
    return [
        CommandHandler("harley", start_chat),
        CommandHandler("end", end_chat),
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    ]
