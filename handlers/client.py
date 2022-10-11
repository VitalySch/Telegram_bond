from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import Bonds
import keyboards
from create_bot import dp, bot
from aiogram.dispatcher import Dispatcher





class BondsSet(StatesGroup):
  price = State()
  year = State()
  bonds = State()
  sorting = State()



async def set_start(message : types.Message):
  await BondsSet.price.set()
  await message.reply('Милорд, введите цену облигаций ниже которой следует искать. Мой господин, разрешите напомнить Вам, что номинальная цена облигаций 1000 рублей')
    

async def set_second(message : types.Message, state=FSMContext):
  async with state.proxy() as data:
    try:
      data['price'] = int(message.text)
      await BondsSet.next()
      await message.reply('Монсеньор, назовите максимальный год погашения облигаций, до которого нам нужно искать')
    except:
      await bot.send_message(message.from_user.id, 'Милор, просто введите число')
  


async def set_third(message : types.Message, state=FSMContext):
  async with state.proxy() as data:
    try:
      data['year'] = int(message.text)
      await BondsSet.next()
      await message.reply('Ваша Светлость, какие облигации Вас интересуют?', reply_markup=keyboards.kb_bonds)
    except:
      await bot.send_message(message.from_user.id, 'Милор, просто просто укажите год')
  


async def set_forth(message : types.Message, state=FSMContext):
  async with state.proxy() as data:
    data['bonds'] = message.text
  await BondsSet.next()
  await message.reply('Ваша Светлость, как сортировать облигации?',  reply_markup=keyboards.kb_set)



async def set_finish(message : types.Message, state=FSMContext):
  data = await state.get_data()
  price = data.get('price')
  year = data.get('year')
  bonds = data.get('bonds')
  sorting = message.text
  
  
  if sorting == '/По цене':
    if bonds == "/Корпоративные":
      a = Bonds.CORP_BONDS(price, year, 1)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас корпоративные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
    
    if bonds == "/ОФЗ":
      a = Bonds.OFZ_BONDS(price, year, 1)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас федеральные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
    
    if bonds == "/Субфедеральные":
      a = Bonds.SUB_BONDS(price, year, 1)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас субфедеральные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')

  elif sorting == '/По купонному доходу':
    if bonds == "/Корпоративные":
      a = Bonds.CORP_BONDS(price, year, 7)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас корпоративные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
    
    if bonds == "/ОФЗ":
      a = Bonds.OFZ_BONDS(price, year, 7)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас федеральные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
    
    if bonds == "/Субфедеральные":
      a = Bonds.SUB_BONDS(price, year, 7)
      await message.reply(f'Мой Господин, вот заинтерисовавшие Вас субфедеральные облигации дешевле {price} рублей, год погашения {year}. Они отсортированы по цене')
      for i in a.bonds_list:      
        await bot.send_message(message.from_user.id, f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
    
    
  await bot.send_message(message.from_user.id, 'Ваша Светлость, это все облигации, которые соответствуют Вашим требованиям на данный момент', reply_markup=keyboards.kb_start)  
  await state.finish()  


def register_handler_client(dp: Dispatcher):
  dp.register_message_handler(set_start, commands=['start', 'help', 'Start', 'Help', 'Старт', 'старт','Помоги', 'помоги'], state=None)
  dp.register_message_handler(set_second, state=BondsSet.price)
  dp.register_message_handler(set_third, state=BondsSet.year)
  dp.register_message_handler(set_forth, state=BondsSet.bonds)
  dp.register_message_handler(set_finish, state=BondsSet.sorting)
  
