import logging
from logging import Logger

from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from data.conf import TOKEN
from handlers import set_handlers


def set_logger() -> Logger:
    lgr = logging.getLogger(__name__)
    lgr.setLevel(logging.WARNING)
    return lgr


def set_startup(dp: Dispatcher) -> None:
    set_handlers(dp)


def start_bot() -> None:
    if not TOKEN:
        raise ValueError(
            "Токен не найден."
        )

    set_logger()

    logging.warning("Logger подключен.")

    bt = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher(bt)

    logging.warning("{} - TOKEN".format(TOKEN))

    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=set_startup(dp)
    )