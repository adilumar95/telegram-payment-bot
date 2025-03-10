from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
import logging

# Replace with your Telegram Payment Bot Token
TOKEN = "7669712107:AAEWoE6dz7oa-n6u9p6PpnoMqtlWwqOU2us"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! You can buy game coins using Telegram Stars.")

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: types.Message):
    stars_spent = message.successful_payment.total_amount / 100  # Convert to Stars
    coins_to_add = stars_spent * 200  # Example: 1 Star = 200 Coins

    user_id = message.from_user.id
    await message.reply(f"✅ Payment successful! {coins_to_add} coins have been added to your account.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_polling(dp, skip_updates=True)
