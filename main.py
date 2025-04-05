# main.py (polling sinovi uchun)
from telegram.ext import Application, MessageHandler, filters
from config import TOKEN
from handlers.group import delete_join_left

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER, delete_join_left))
app.run_polling()