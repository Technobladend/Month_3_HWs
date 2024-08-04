from aiogram import types, Dispatcher


async def echo_handler(message: types.Message):
    if message.text.isdigit():
        digit = int(message.text)
        await message.answer(digit**2)
    else:
        await message.answer(message.text)


def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
