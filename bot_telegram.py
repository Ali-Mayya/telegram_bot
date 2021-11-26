from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from create_bot import dp
import warnings
warnings.filterwarnings("ignore")

import os
# TOKEN="2100679408:AAHTdh7sJFK3m1uu9TtPVMqQlNWn2q3WfDE"
# # os.getenv('TOKEN'))
# bot=Bot(token=TOKEN)
# dp=Dispatcher(bot)


async def on_satrter(_):
    print("bot is online ")

import client1, admin , other
other.register_handlers_other(dp)
client1.register_handlers_client(dp)
admin.register_handlers_adnmin(dp)
'''********************************client part ***********************'''
# @dp.message_handler(commands=['start','help'])
# async def command_start(message:types.Message):
#     try:
#         await bot.send_message(message.from_user.id,"bon appetite")
#         await message.delete()
#     except:
#         await message.reply("chatting with bot in private , write him there")
#
#
# @dp.message_handler(commands=['regime'])
# async def store_open_command(message:types.Message):
#     await bot.send_message(message.from_user.id, "St-fr from 9:00 to 20:00")
#
# @dp.message_handler(commands=["location"])
# async  def store_plave_command(message:types.Message):
#     await bot.send_message(message.from_user.id," shosse v lavriki ")
#     await message.reply("shosse v lavriki ")
#





'''********************************adminstartor part ***********************'''
















'''********************************common part ***********************'''



#
# @dp.message_handler()
#
# async def echo_send(message : types.Message):
#     # if message.text=="привет":
#     #     await message.answer('hello how are u ')
#     # await message.reply(message.text)
#     await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp,skip_updates=True, on_startup=on_satrter)