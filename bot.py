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

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.reply("Welcome! You can buy game coins using Telegram Stars.")

@dp.message(lambda message: message.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: Message):
    stars_spent = message.successful_payment.total_amount / 100  # Convert to Stars
    coins_to_add = stars_spent * 200  # Example: 1 Star = 200 Coins

    user_id = message.from_user.id
    await message.reply(f"✅ Payment successful! {coins_to_add} coins have been added to your account.")

async def main():
    """ Main entry point for the bot """
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))

# 🔹 Dummy Web Server to Keep Render Happy
async def handle_request(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get("/", handle_request)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    web.run_app(app, port=int(os.getenv("PORT", 8080)))  # Render requires a port
