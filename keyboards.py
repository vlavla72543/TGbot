from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


help_keyboard = InlineKeyboardMarkup().\
    add(InlineKeyboardButton('Купить Discord Nitro', callback_data='price')).\
    add(InlineKeyboardButton('Новости Discord`а', callback_data='news'))


price_keyboard = InlineKeyboardMarkup().\
    add(InlineKeyboardButton('1 месяц', callback_data='1_month')).\
    add(InlineKeyboardButton('3 месяца', callback_data='3_month')).\
    add(InlineKeyboardButton('12 месяцев', callback_data='12_month'))
