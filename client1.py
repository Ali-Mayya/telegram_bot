from aiogram import types, Dispatcher
from create_bot import dp, bot
# from keybords import client_kb
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
b1=KeyboardButton('/Здравствуйте')
# b2=KeyboardButton("/location")
# b3=KeyboardButton("menue")

kb_client=ReplyKeyboardMarkup()

kb_client.add(b1)






@dp.message_handler(commands=['start','help'])
async def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id,"Welcome to happy Pizza restaurant , How can i help u ", reply_markup=kb_client)
        await bot.send_message(message.from_user.id,"to order pizza press the button Здравствуйте ", reply_markup=kb_client)

        await message.delete()
    except:
        await message.reply("chatting with bot in private , write him there")


@dp.message_handler(commands=['regime'])
async def store_open_command(message:types.Message):
    await bot.send_message(message.from_user.id, "we work St-fr from 9:00 to 20:00")

@dp.message_handler(commands=["location"])
async  def store_place_command(message:types.Message):
    await bot.send_message(message.from_user.id," our location is shosse v lavriki ")
    # await message.reply("shosse v lavriki ")

'''*****************************dialog ******************************************'''

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from create_bot import dp
from aiogram import types,Dispatcher

abstract={"болшьшую":1,"Маленькую":2,"катрой":3,"наличкой":4 }
summary=[]

class FSM_admin(StatesGroup):
    # question=State()
    size=State()
    payment=State()
    summary=State()
    confirm=State()



@dp.message_handler(commands=['Здравствуйте'],state=None)
async def cm_start(message:types.Message):
    await FSM_admin.size.set()
    await message.reply("Какую вы хотите пиццу? Большую или маленькую?")

@dp.message_handler(state=FSM_admin.size)
async  def load_size(message:types.Message):
    # async with state.proxy() as data:
    #     data['question']=message.text
    if (message.text in ['Большую' ,'Маленькую','большую' ,'маленькую']):
        await FSM_admin.next()
        await message.reply("Как вы будете платить? ")
        summary.append(message.text)

    else:
        await message.reply("выбираете пожалуйста лтбо большую либо Маленкую ")
        @dp.message_handler(state=FSM_admin.size)
        async def load_size(message: types.Message):
            # async with state.proxy() as data:
            #     data['question']=message.text
            summary.append(message.text)


@dp.message_handler( state=FSM_admin.payment)
async def load_payment(message: types.Message):
    # async with state.proxy() as data:
    #     data['name'] = message.text
    summary.append(message.text)
    await FSM_admin.next()
    await message.reply(f'Вы хотите {summary[0]} пиццу, оплата - {summary[1]}?')


@dp.message_handler( state=FSM_admin.summary)
async def load_summary(message: types.Message):
    # async with state.proxy() as data:
    #     data['dscription'] = message.text
    await FSM_admin.next()
    await message.reply("Спасибо за заказ  ")



# @dp.message_handler( state=FSM_admin.price)
# async def load_price(message: types.Message):
#     await message.reply("asasasas")








def register_handlers_client(dp):
    dp.register_message_handler(command_start,commands=['start','help'])
    dp.register_message_handler(store_open_command, commands=['regime'])
    dp.register_message_handler(store_place_command, commands=['location'])