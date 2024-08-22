from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import Hw_3.buttons as buttons
import re
from aiogram.types import ReplyKeyboardRemove


class FSM_store(StatesGroup):
    product_name = State()
    product_size = State()
    product_category = State()
    product_price = State()
    product_photo = State()
    confirm = State()

async def fsm_start(message: types.Message):
    await message.answer(text="Welcome\n"
                              "Please enter product details!\n\n"
                              "Enter product's name:")
    await FSM_store.product_name.set()


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

    await FSM_store.next()
    await message.answer(text='choice size:', reply_markup=buttons.product_size_button)


async def load_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # sizes = ['S', 'M', 'L', 'XL', '3XL']
        data['product_size'] = message.text


    rm_kb = types.ReplyKeyboardRemove()
    await FSM_store.next()
    await message.answer(text="Enter product's category:", reply_markup=rm_kb)


async def load_product_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_category'] = message.text

    await FSM_store.next()
    await message.answer(text="Enter product's price:")


async def load_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_price'] = message.text

    await message.answer(text="Send a photo of product:")
    await FSM_store.next()


async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['product_photo'],
                               caption=f"Product's name: {data['product_name']}\n\n"
                               f"Product's size: {data['product_size']}\n\n"
                               f"Product's category: {data['product_category']}\n\n"
                               f"Product's price: {data['product_price']}\n\n"
                                       f"**Is the data correct?**", parse_mode="Markdown",
                               reply_markup=buttons.yes_no
                               )
    await FSM_store.confirm.set()


async def confirm_data(message: types.Message, state: FSMContext):
    if message.text == 'Yes':
        await message.answer("Data is Saved!", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Cancel. Data is deleted.", reply_markup=ReplyKeyboardRemove())

    await state.finish()



def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(fsm_start,
                                commands=['product', 'store'])
    dp.register_message_handler(load_product_name,
                                state=FSM_store.product_name)
    dp.register_message_handler(load_product_size,
                                state=FSM_store.product_size)
    dp.register_message_handler(load_product_category,
                                state=FSM_store.product_category)
    dp.register_message_handler(load_product_price,
                                state=FSM_store.product_price)
    dp.register_message_handler(load_product_photo, content_types=['photo'],
                                state=FSM_store.product_photo)
    dp.register_message_handler(confirm_data, state=FSM_store.confirm, content_types=['text'])
