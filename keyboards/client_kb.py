from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



b1 = KeyboardButton("/start")

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.add(b1)

corp = KeyboardButton("/Корпоративные")
ofz = KeyboardButton("/ОФЗ")
sub = KeyboardButton("/Субфедеральные")
kb_bonds = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_bonds.add(corp).insert(ofz).add(sub)




a1 = KeyboardButton("/По цене")
a2 = KeyboardButton("/По купонному доходу")
kb_set = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_set.add(a1).add(a2)