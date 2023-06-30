from typing import (
    Union,
    TextIO,
    BinaryIO
)
import logging

import yadisk


class InitializeDisk:
    def __init__(self, token: str) -> None:
        if not isinstance(token, str):
            raise TypeError(
                "Токен не str,\n {}".format(
                    token.__repr__()
                )
            )
        super().__init__()
        self._app = yadisk.YaDisk(token=token)
        if self._app.check_token(token) == False:
            raise TypeError(
                "Токен невалидный: {}".format(
                    token
                )
            )


    def check_structure(self) -> bool:
        return (
            self._app.is_dir('/crisis-bot')
            and self._app.is_dir('disk:/crisis-bot/metro')
            and self._app.is_dir('disk:/crisis-bot/street')
            and self._app.is_dir('disk:/crisis-bot/club')
        )


    def create_structure(self) -> bool:
        """Структура такая:\n
        tgbot-crisis --> metro\n
                     |-> street\n
                     '-> club\n

        Хранение записей ввиде "datetime_unix-sha256(login-tg)"
        Например
        "1685206276-2631b9bc38ef6afcd6c06b669ee0a31912013f0f37db2578a52e5b83a3ea8c59"
        (27.05.23:hh:mm:ss - spbdqs)
        """
        if self.check_structure():
            logging.info("Структура уже создана!")
            return True
        try:
            root_dir = self._app.mkdir('/crisis-bot')
            self._app.mkdir(root_dir.path + '/metro')
            self._app.mkdir(root_dir.path + '/street')
            self._app.mkdir(root_dir.path + '/club')
            return self.check_structure()
        except Exception as e:
            logging.critical(
                "Обнаружена ошибка при составлении корневой директории в Я.Диске",
                e.__repr__()
            )
            return False
    

    def delete_structure(self, trash: bool = False) -> bool:
        """Удаляем структуру и всё что в ней.
        Удаление корзины опционально. (удаляется вся корзина)
        """
        try:
            self._app.remove('/crisis-bot')
            if trash:
                self._app.remove_trash('/')
            return True
        except Exception as e:
            logging.critical(
                "Обнаружена ошибка при удалении корневой директории в Я.Диске",
                e.__repr__()
            )
            return False



class Upload:
    def __init__(self, app: yadisk.YaDisk) -> None:
        if not isinstance(app, yadisk.YaDisk):
            raise TypeError(
                "Передавайте верно объект Яндекс Диска,\n {}".format(
                    type(app)
                )
            )
        super().__init__()
        self._app = app

    def upload(self, obj: Union[TextIO, BinaryIO]) -> bool:
        logging.info("File: {}\ntype: {}".format(obj.name, type(obj)))

        self._app.upload(obj, '/')