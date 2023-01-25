from aiogram import Dispatcher

from bot.handlers.user import register_user_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_user_handlers,
    )
    for handler in handlers:
        handler(dp)