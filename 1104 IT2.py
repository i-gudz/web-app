from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6673079767:AAH4qSwy1Dtg2GUEQAtW29oLMCBgEuN0uWs')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open web-app", web_app=WebAppInfo(url = 'https://rozetka.com.ua/ua/')))
    await message.answer("Hello, my friend!!!", reply_markup=markup)


executor.start_polling(dp)