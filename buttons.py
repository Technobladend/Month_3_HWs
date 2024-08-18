from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отмена')
)

submit_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Да'),
    KeyboardButton('Нет')
)


product_size_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('S'),
    KeyboardButton('M'),
    KeyboardButton('L'),
    KeyboardButton('XL'),
    KeyboardButton('3XL')
)

yes_no = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Yes'),
    KeyboardButton('No')
)