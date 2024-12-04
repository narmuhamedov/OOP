from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Токен
TOKEN = '7714152662:AAF5a70mmcJJKlyXr9tT3SMJV9t2FVwMEdY'

# Создание бота
bot = Bot(token=TOKEN)

# Создание маршрутизатора
router = Router()

# Викторина
quiz_data = [
    {
        "question": 'Как тебя зовут?',
        "image": 'image/game_club.png',
        "options": ['Радомир', 'Адилет', 'Арафат', 'Асема'],
        "correct": "Радомир"
    },
    {
        "question": 'Сколько вам лет?',
        "image": 'image/it_club.png',
        "options": ['22', '21', '16', '27'],
        "correct": "27"
    },
    {
        "question": 'Какой ты тип разработчика?',
        "image": 'image/k-pop.png',
        "options": ['Backend', 'Fullstack', 'Devops', 'Student'],
        "correct": "Fullstack"
    },
]

user_data = {}


@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Привет! Я твой новый Telegram бот Иван")


@router.message(Command("quiz"))
async def start_quiz(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"current_question": 0, "score": 0}
    await send_question(user_id)


async def send_question(user_id):
    user_state = user_data[user_id]
    question_index = user_state["current_question"]
    if question_index < len(quiz_data):
        question = quiz_data[question_index]
        image = FSInputFile(question["image"])
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=option, callback_data=option) for option in question["options"]]
            ]
        )
        await bot.send_photo(
            user_id,
            photo=image,
            caption=question["question"],
            reply_markup=keyboard
        )
    else:
        await bot.send_message(user_id, f"Викторина завершена: {user_state['score']} из {len(quiz_data)}")


@router.callback_query()
async def handle_answer(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_data:
        await callback.answer('Начните викторину с команды /quiz')
        return

    user_state = user_data[user_id]
    question_index = user_state["current_question"]
    question = quiz_data[question_index]

    # Проверка на правильность ответа
    if callback.data == question["correct"]:
        user_state['score'] += 1
        await callback.answer('Правильно!')
    else:
        await callback.answer('Неправильно!')

    user_state['current_question'] += 1
    await send_question(user_id)


async def main():
    dp = Dispatcher()  # Создание диспетчера
    dp.include_router(router)  # Подключение маршрутизатора

    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
