import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import help_keyboard, price_keyboard
from parser import get_blog, get_collection


API_TOKEN = ''
DISCORD_LINK = 'https://discord.com/'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = "Привет, с помощью этого бота ты можешь купить Discord Nitro или узнать последние новости Discord'a"
    await message.answer(text, reply_markup=help_keyboard)


async def send_price(message: types.Message):
    with open('img/discord_nitro.jpeg', 'rb') as img:
        await bot.send_photo(message.chat.id, photo=img, caption='Выберите подписку:', reply_markup=price_keyboard)


async def send_news(message: types.Message):
    collection_url = get_collection(DISCORD_LINK)
    data = get_blog(collection_url)
    if data['media']:
        await bot.send_photo(message.chat.id, photo=data['media'])
    news_keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Оригинал', url=data['media']))
    await message.answer(data['text'], reply_markup=news_keyboard)


@dp.callback_query_handler()
async def callbacks(callback: types.CallbackQuery):
    if callback.data == 'price':
        await send_price(callback.message)
        await callback.message.delete()
    if callback.data == 'news':
        await send_news(callback.message)
        await callback.message.delete()
    if callback.data == '1_month':
        await callback.answer('Вы купили подписку')
        await callback.message.delete()
    if callback.data == '3_month':
        await callback.answer('Вы купили подписку')
        await callback.message.delete()
    if callback.data == '12_month':
        await callback.answer('Вы купили подписку')
        await callback.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
