import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType
from aiohttp import web

# 🔹 Replace with your actual Telegram Bot Token
TOKEN = "7669712107:AAEWoE6dz7oa-n6u9p6PpnoMqtlWwqOU2us"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Logging
logging.basicConfig(level=logging.INFO)
logging.info("🚀 Bot is starting...")

@dp.message(CommandStart())
async def send_welcome(message: Message):
    logging.info(f"📩 Received message: {message.text} from {message.from_user.id}")
    await message.reply("Welcome! You can buy game coins using Telegram Stars.")

@dp.message(lambda message: message.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: Message):
    stars_spent = message.successful_payment.total_amount / 100  # Convert to Stars
    coins_to_add = stars_spent * 200  # Example: 1 Star = 200 Coins

    user_id = message.from_user.id
    logging.info(f"💰 Payment received: {stars_spent} Stars from {user_id}")
    await message.reply(f"✅ Payment successful! {coins_to_add} coins have been added to your account.")

# 🔹 Dummy Web Server to Keep Render Happy
async def handle_request(request):
    return web.Response(text="Bot is running!")

async def run_web_server():
    """ Starts a dummy web server for Render """
    logging.info("🌐 Starting web server on port 8080...")
    app = web.Application()
    app.router.add_get("/", handle_request)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=int(os.getenv("PORT", 8080)))
    await site.start()

async def main():
    """ Start both the bot polling and the web server """
    logging.info("✅ Starting bot polling and web server...")
    asyncio.create_task(run_web_server())  # Run web server in the background
    await dp.start_polling(bot)  # Start bot polling

# 🔹 Start the bot and web server in the same event loop
if __name__ == "__main__":
    asyncio.run(main())
