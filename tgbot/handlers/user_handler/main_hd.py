from typing import Dict
from pathlib import Path

from aiogram import types

from keyboard import (
    MainKeys,
    ListenKeys,
    TellingKeys
)


dest = Path(__file__).parent.parent.parent

class MainHandlers:
    tl_id_to_slg: Dict[int, str] = {}

    telling_keys = {
        "telling-metro": "metro",
        "telling-street": "street",
        "telling-club": "club"
    }
    listen_keys = (
        "listen-metro",
        "listen-street",
        "listen-club"
    )


    async def start(msg: types.Message):
        await msg.answer(
            '''Выбери, что ты хочешь сделать:
            ''',
            reply_markup=MainKeys().markup
        )


    @classmethod
    async def listen_telling(cls, msg: types.Message):
        print(msg.from_id)
        usr_id = msg.from_id
        print(dest)
        from hashlib import sha256
        from time import time

        # if usr_id in cls.tl_id_to_slg.keys():
        await msg.voice.download(
            # destination_dir=dest,
            destination_file="{}-{}.mp3".format(
                str(int(time())),
                str(sha256(bytes(usr_id)).hexdigest())
            )
        )
        # else:
        #     await msg.answer(
        #         """Прежде, чем отправлять историю выберите категорию.
        #         """
        #     )


    @classmethod
    async def listen_callbacks(cls, callback: types.CallbackQuery):
        clbk: dict = callback.to_python()
        clbk_data: str = clbk.get('data')
        id_usr = callback.message.chat.id

        if clbk_data == 'listen':
            await callback.message.answer(
                text='''Выбери куда ты хочешь отправится?
                ''',
                reply_markup=ListenKeys().markup
            )

        elif clbk_data == 'telling':
            await callback.message.answer(
                text='''Расскажи историю и 
                ''',
                reply_markup=TellingKeys().markup
            )
        
        elif clbk_data in cls.listen_keys:
            ...
        
        elif clbk_data in cls.telling_keys.keys():
            await callback.message.answer(
                text='''Рассказывай историю''',
            )
            print(id_usr, clbk_data)
            if cls.tl_id_to_slg.get(id_usr):
                ... # печать что категория поменяна
            cls.tl_id_to_slg[id_usr] = cls.telling_keys[clbk_data]
            print(cls.tl_id_to_slg)
