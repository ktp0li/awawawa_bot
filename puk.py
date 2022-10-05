#!/usr/bin/env python
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
token = ""
bot = Bot(token=token)

dp = Dispatcher(bot, storage=MemoryStorage())


class userstate(StatesGroup):
    encode = State()
    decode = State()


@dp.message_handler(state='*', commands=['decode'])
async def decode_command(message: types.Message):
    await message.reply("type awawawa to decode")
    await userstate.decode.set()


@dp.message_handler(state='*', commands=['encode'])
async def encode_command(message: types.Message):
    await message.reply("type awawawa to encode")
    await userstate.encode.set()


@dp.message_handler(state=userstate.decode)
async def decode(message: types.Message, state: FSMContext):
    await message.reply("".join(chr(int(i.replace('a', '0')
                                        .replace('w', '1'), 2)) for i in
                                message.text.split()))


@dp.message_handler(state=userstate.encode)
async def encode(message: types.Message, state: FSMContext):
    await message.reply("".join(bin(ord(i)).replace('0b', '')
                                .replace('0', 'a').replace('1', 'w')
                                + ' ' for i in message.text))


if __name__ == '__main__':
    executor.start_polling(dp)
