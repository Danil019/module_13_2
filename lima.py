from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7663863093:AAHBqmiFkF15GWjTPKjsmgb68wyN-Iz8QVg"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands = 'start')
async def hello_word(message):
    print('Привет! Я бот помогающий твоему здоровью. Но это не точно')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)