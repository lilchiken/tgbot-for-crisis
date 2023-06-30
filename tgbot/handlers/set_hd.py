from aiogram import Dispatcher
from aiogram import types


from handlers.user_handler.main_hd import MainHandlers


def set_handlers(dp: Dispatcher) -> bool:
    if not MainHandlers:
        raise ValueError("No handlers")
    dp.register_message_handler(
        MainHandlers.start,
        commands=["start"]
    )
    dp.register_callback_query_handler(
        MainHandlers.listen_callbacks,
        lambda callback: True
    )
    dp.register_message_handler(
        MainHandlers.listen_telling,
        content_types=types.ContentType.VOICE,
    )

