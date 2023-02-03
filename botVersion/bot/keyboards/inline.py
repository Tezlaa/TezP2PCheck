from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


settings = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Notification", callback_data="settings_notification"),
    InlineKeyboardButton("Fiat", callback_data=""),
    InlineKeyboardButton("Asset", callback_data=""),
    InlineKeyboardButton("Bank", callback_data=""),
    InlineKeyboardButton("Profile", callback_data=""),
)