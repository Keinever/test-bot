from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import bot_token

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_of_bot(message: Message):
    await message.answer("Привет я твой личный помощник, меня зовут Woppy.\
                        Пиши не стесняйся")


@dp.message(Command(commands=["help"]))
async def help_for_user(message: Message):
    await message.answer("Пиши не стесняйся, помогу чем смогу!")


if __name__ == '__main__':
    dp.run_polling(bot)
