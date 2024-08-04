from aiogram import types
import logging
from aiogram.utils import executor
from config import dp
from handlers import commands, echo


commands.register_commands(dp)


echo.register_echo_handler(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
