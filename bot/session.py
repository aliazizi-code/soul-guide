from telegram import Update
from telegram.ext import ContextTypes
from core.ai_client import chat_with_harley

user_sessions: dict[int, bool] = {}

async def start_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_sessions[user_id] = True
    await update.message.reply_text("چت با هارلی شروع شد. راحت باش و حرف بزن.")

async def end_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_sessions.pop(user_id, None)
    await update.message.reply_text("چت با هارلی به پایان رسید. هر وقت خواستی برگرد.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_sessions.get(user_id, False):
        reply = chat_with_harley(user_id, text)
        await update.message.reply_text(reply)
    else:
        await update.message.reply_text("برای شروع چت با هارلی از /harley استفاده کن.")
