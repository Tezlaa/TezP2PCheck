from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from botVersion.bot.handlers.user.main import settings

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).insert(
    KeyboardButton("Information")).insert(KeyboardButton("Settings")).insert(KeyboardButton("Parse"))

back_to_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).insert(
    KeyboardButton("Back to menu"),
)
