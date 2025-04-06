from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import random

BOT_TOKEN = "7904632196:AAGkTwBBfZlC4lG0n-bugC07srivYbxSSXA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        "Я бот с игрой в число и с другими функциями:\n"
        "/start - начало\n"
        "/about - информация\n"
        "/random - случайное число\n"
        "/photo - фото\n"
        "/innopolis - сайт\n"
        "/menu - кнопки управления"
    )

@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer(
        "🤖 <b>О боте:</b>\n"
        "• Кнопки и фото\n"
        "• Есть меню /menu\n"
        "• Может играть в число\n"
        "• Покажит сайт",
        parse_mode="HTML",
        disable_web_page_preview=True
    )

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    await message.answer(f"🎲 Случайное число: <b>{random.randint(1, 100)}</b>", parse_mode="HTML")

@dp.message(Command("innopolis"))
async def cmd_innopolis(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Открыть сайт Иннополиса",
        url="https://innopolis.university"
    ))
    await message.answer(
        text="🌐 Нажмите кнопку ниже, чтобы перейти на сайт:",
        reply_markup=builder.as_markup()
    )

@dp.message(Command("photo"))
async def cmd_photo(message: types.Message):
    await message.answer_photo(
        photo="https://www.ridus.ru/images/2022/9/13/1509694/in_article_webp_3771d7439b.webp",
        caption="📸 Изображение"
    )

@dp.message(Command("menu"))
async def cmd_menu(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="🎲 Рандом"),
        types.KeyboardButton(text="📸 Фото"),
    )
    builder.row(
        types.KeyboardButton(text="🌐 Иннополис"),
        types.KeyboardButton(text="❓ О боте")
    )
    await message.answer(
        "Главное меню:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )


@dp.message(lambda msg: msg.text in ["🎲 Рандом", "📸 Фото", "🌐 Иннополис", "❓ О боте"])
async def handle_reply_buttons(message: types.Message):
    if message.text == "🎲 Рандом":
        await cmd_random(message)
    elif message.text == "📸 Фото":
        await cmd_photo(message)
    elif message.text == "🌐 Иннополис":
        await cmd_innopolis(message)
    else:
        await cmd_about(message)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
