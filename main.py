# main.py
import os
import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from config import TOKEN
from handlers.group import delete_join_left

async def webhook_handler(request):
    """Telegramdan kelgan xabarni qabul qilish"""
    try:
        data = await request.json()
        update = Update.de_json(data, app.bot)
        await app.process_update(update)
        return web.Response(text="OK")
    except Exception as e:
        print(f"Webhook xatosi: {str(e)}")
        return web.Response(text="Error", status=500)

async def main():
    global app
    app = Application.builder().token(TOKEN).build()

    # Handler’lar
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER, delete_join_left))

    # Webhook sozlamasi
    webhook_url = os.environ.get("WEBHOOK_URL", "https://your-app-name.onrender.com")
    await app.bot.set_webhook(url=webhook_url)
    print(f"Webhook o‘rnatildi: {webhook_url}")

    # Server
    aiohttp_app = web.Application()
    aiohttp_app.router.add_post("/", webhook_handler)
    runner = web.AppRunner(aiohttp_app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8443))  # Render portni o‘zi beradi
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    await app.initialize()
    await app.start()
    print("Bot webhook rejimida ishlayapti!")
    await asyncio.Event().wait()  # Botni doimiy ishlashda ushlab turish

if __name__ == "__main__":
    asyncio.run(main())