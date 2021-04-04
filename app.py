import logging
from aiogram import Bot, Dispatcher, executor, types

from config import config
import greeting

logging.basicConfig(level=logging.ERROR,
                    filename='bot.log',
                    format='%(asctime)s %(name)s: %(levelname)s [%(process)d] %(message)s')
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = (message.from_user.first_name + ' ' + message.from_user.last_name)
    user = greeting.Student(user_id, user_name)
    await message.answer(f'Привет, {user.name}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
