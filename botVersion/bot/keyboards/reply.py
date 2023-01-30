from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).insert(
    KeyboardButton("Information")).insert(KeyboardButton("Setings")).insert(KeyboardButton("Parse"))

