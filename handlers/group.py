# handlers/group.py
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

async def delete_join_left(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if update.message.new_chat_members or update.message.left_chat_member:
            await update.message.delete()
            logging.info(f"Join/left xabar o‘chirildi: chat_id={update.effective_chat.id}")
    except Exception as e:
        logging.error(f"Xabar o‘chirish xatosi: {str(e)}")