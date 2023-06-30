from aiogram import types


class MainKeys:
    def __init__(self) -> None:
        self.story_tell = types.InlineKeyboardButton(
            text="Рассказать историю",
            callback_data="telling"
        )
        self.story_listen = types.InlineKeyboardButton(
            text="Послушать историю",
            callback_data="listen"
        )
        self.markup = types.InlineKeyboardMarkup().add(
            self.story_listen,
            self.story_tell,
        )


class ListenKeys:
    def __init__(self) -> None:
        self.metro = types.InlineKeyboardButton(
            text="В метро",
            callback_data="listen-metro"
        )
        self.street = types.InlineKeyboardButton(
            text="На улице",
            callback_data="listen-street"
        )
        self.club = types.InlineKeyboardButton(
            text="В клубе",
            callback_data="listen-club"
        )
        self.markup = types.InlineKeyboardMarkup().add(
            self.metro,
            self.street,
            self.club,
        )


class TellingKeys:
    def __init__(self) -> None:
        self.metro = types.InlineKeyboardButton(
            text="Метро",
            callback_data="telling-metro"
        )
        self.street = types.InlineKeyboardButton(
            text="Улица",
            callback_data="telling-street"
        )
        self.club = types.InlineKeyboardButton(
            text="Клуб",
            callback_data="telling-club"
        )
        self.markup = types.InlineKeyboardMarkup().add(
            self.metro,
            self.street,
            self.club,
        )
