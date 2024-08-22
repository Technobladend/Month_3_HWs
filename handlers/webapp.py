from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from HW_6.config import dp


async def webapp_reply_button(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    geeks_online = KeyboardButton("Geeks Online",
                                  web_app=types.WebAppInfo(url="https://online.geeks.kg"))
    kaktus_media = KeyboardButton("Кактус Медиа",
                                  web_app=types.WebAppInfo(url="https://kaktus.media"))
    Netflix = KeyboardButton("Netflix",
                             web_app=types.WebAppInfo(url="https://www.netflix.com/"))
    Youtube = KeyboardButton("Youtube",
                             web_app=types.WebAppInfo(url="https://www.youtube.com/"))
    Twitch = KeyboardButton("Twitch",
                             web_app=types.WebAppInfo(url="https://www.twitch.com/"))
    Chess = KeyboardButton("Chess",
                             web_app=types.WebAppInfo(url="https://www.chess.com/"))
    MangaLib = KeyboardButton("MangaLib",
                             web_app=types.WebAppInfo(url="https://mangalib.me/"))
    Facebook = KeyboardButton("Facebook",
                             web_app=types.WebAppInfo(url="https://www.facebook.com//"))

    keyboard.add(geeks_online, kaktus_media, Netflix, Youtube, Twitch, Chess, MangaLib, Facebook)

    await message.answer(text='Нажми на кнопки для открытия сайтов', reply_markup=keyboard)


async def webapp_inline_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

    geeks_online = InlineKeyboardButton("Geeks", url="https://online.geeks.kg")

    kaktus_media = InlineKeyboardButton("Кактус Медиа", url="https://kaktus.media")

    Netflix = InlineKeyboardButton("Netflix", url="https://www.netflix.com/kg-ru/")

    jutsu = InlineKeyboardButton('Jut.Su', url="https://jut.su/")

    Youtube = InlineKeyboardButton("Youtube", url='https://www.youtube.com/')

    Twitch = InlineKeyboardButton("Twitch", url="https://www.twitch.com/")

    Chess = InlineKeyboardButton("Chess", url="https://www.chess.com/")

    MangaLib = InlineKeyboardButton("MangaLib", url="https://mangalib.me/")

    Facebook = InlineKeyboardButton("Facebook", url="https://www.facebook.com//")

    keyboard.add(geeks_online, kaktus_media, Netflix, jutsu, Youtube, Twitch, Chess, MangaLib, Facebook)

    await message.answer(text='Нажми на кнопки для открытия сайтов', reply_markup=keyboard)


def register_webapp_handlers(dispatcher: Dispatcher):
    dp.register_message_handler(webapp_reply_button, commands=['webreply'])
    dp.register_message_handler(webapp_inline_button, commands=['webinline'])
