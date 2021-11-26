from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from create_bot import dp
from aiogram import types,Dispatcher

class FSM_admin(StatesGroup):
    question=State()
    name=State()
    description=State()
    price=State()



@dp.message_handler(commands=['load'],state=None)
async def cm_start(message:types.Message):
    await FSM_admin.question.set()
    await message.reply("upload photo")

@dp.message_handler(state=FSM_admin.question)
async  def load_photo(message:types.Message):
    # async with state.proxy() as data:
    #     data['question']=message.text
        await FSM_admin.next()
        await message.reply("enetr the name ")


@dp.message_handler( state=FSM_admin.name)
async def load_name(message: types.Message):
    # async with state.proxy() as data:
    #     data['name'] = message.text
        await FSM_admin.next()
        await message.reply("enetr discrption ")


@dp.message_handler( state=FSM_admin.description)
async def load_Description(message: types.Message):
    # async with state.proxy() as data:
    #     data['dscription'] = message.text
        await FSM_admin.next()
        await message.reply("enetr price ")


@dp.message_handler( state=FSM_admin.price)
async def load_price(message: types.Message):
    await message.reply("asasasas")


    # async with state.proxy() as data:
    #     data['price'] = float(message.text)

        # async with state.proxy()as data:
        #     await message.reply(str(data))

        # await state.finish()

def register_handlers_adnmin(dp:Dispatcher):
    dp.register_message_handler(cm_start,commands='upload',state=None)
    dp.register_message_handler(load_photo,
                                state = FSM_admin.question)
    dp.register_message_handler(load_name,state=FSM_admin.name)
    dp.register_message_handler(load_Description,state=FSM_admin.description)
    dp.register_message_handler(load_price,state=FSM_admin.price)








