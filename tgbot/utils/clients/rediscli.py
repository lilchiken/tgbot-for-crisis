import logging

import redis

from utils.patterns.mixins import SingletonConnectionMixinMeta


logging.basicConfig(level=logging.INFO)


class RedisCli(metaclass=SingletonConnectionMixinMeta):
    """TODO: create methods for get/post/delete in hash."""


    def __init__(
        self,
        name_hash:str="tgbot-criris"
    ) -> None:
        self._redis = redis.Redis(
            host="localhost",
            port=6379,
            max_connections=2,
            db=10
        )
        self.name_hash = name_hash

        self.lgr = logging.getLogger("loggerRedis")


    @property
    def redis(self) -> redis.Redis:
        return self._redis


    @redis.setter
    def set_redis(
        self,
        host:str="localhost",
        port:int=6379,
        max_connections:int=2,
        db:int=10
    ) -> None:
        _old_redis = self._redis
        self._redis = redis.Redis(
            host=host,
            port=port,
            max_connections=max_connections,
            db=db
        )

        if not self.try_connection():
            self.lgr.warning(
                "Bad set for redis.\nself._redis stay prev ver"
            )
            self._redis = _old_redis
    

    def __hget_check(self) -> bool:
        get = self.redis.hget(
            self.name_hash,
            key="my-git"
        )
        if get:
            return True
        return False
    

    def __hset_check(self) -> bool:
        set = self.redis.hset(
            self.name_hash,
            key="my-git",
            value="lilchiken"
        )
        if set:
            return True
        return False


    def try_connection(self) -> bool:
        if self.__hget_check():
            return True
        self.__hset_check()
        print('y')
        if self.__hget_check():
            return True
        return False


    def hash_set(self, )
        


aio = RedisCli()
# print(aio)
# f = aio.try_connection()
# print(f)
