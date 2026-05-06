import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

# Вставьте сюда ваш токен от @BotFather
TOKEN = "ВАШ_ТОКЕН_БОТА"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    # Создаем строитель клавиатуры
    builder = InlineKeyboardBuilder()
    
    # Первая кнопка: Ссылка на оплату (открывается как WebApp или просто ссылка)
    builder.row(types.InlineKeyboardButton(
        text="🛍 Xaridni Boshlash", 
        web_app=WebAppInfo(url="https://fikostrimit.github.io/fiko-pay/")
    ))
    
    # Вторая кнопка: Ссылка на канал
    builder.row(types.InlineKeyboardButton(
        text="📢 Yangiliklar kanali", 
        url="https://t.me/FEKOXD"
    ))

    welcome_text = (
        "<b>Xush kelibsiz!</b>\n\n"
        "Bizni xizmatlarimizdan foydalaning, vaqtingizni va pulingizni tejang.\n\n"
        "Bizning xizmatlarimizdan foydalanganingiz uchun rahmat!"
    )

    await message.answer(
        welcome_text, 
        reply_markup=builder.as_markup(),
        parse_mode="HTML"
    )

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
