import logging
from datetime import datetime

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
        logging.basicConfig(level=logging.INFO)
        self.lgr = logging.getLogger("lgrYaDisk")


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
            self.lgr.info("Структура уже создана!")
            return True
        try:
            root_dir = self._app.mkdir('/crisis-bot')
            self._app.mkdir(root_dir.path + '/metro')
            self._app.mkdir(root_dir.path + '/street')
            self._app.mkdir(root_dir.path + '/club')
            self.lgr.info("Структура создана {}".format(datetime.now()))
            return self.check_structure()
        except Exception as e:
            self.loger.critical(
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
            self.lgr.info("Структура удалена {}".format(datetime.now()))
            return True
        except Exception as e:
            self.loger.critical(
                "Обнаружена ошибка при удалении корневой директории в Я.Диске",
                e.__repr__()
            )
            return False


