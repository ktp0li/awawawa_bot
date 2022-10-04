#!/usr/bin/env python
import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)
token = ""
bot = Bot(token=token)

dp = Dispatcher(bot)


@dp.message_handler(commands=['decode'])
async def decode_command(message: types.Message):
    await message.reply("type awawawa to decode")

    @dp.message_handler()
    async def decode(message: types.Message):
        #  await message.reply(message.text)
        await message.reply("".join(chr(int(i.replace('a', '0')
                                            .replace('w', '1'), 2)) for i in
                                    message.text.split()))


@dp.message_handler(commands=['encode'])
async def encode_command(message: types.Message):
    await message.reply("type awawawa to encode")

    @dp.message_handler()
    async def encode(message: types.Message):
        await message.reply("".join(bin(ord(i)).replace('0b', '')
                                    .replace('0', 'a').replace('1', 'w')
                                    + ' ' for i in message.text))


if __name__ == '__main__':
    executor.start_polling(dp)
