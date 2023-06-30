class ConnectionCaller(type):

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        __bool = obj.try_connection()
        if not __bool:
            raise ConnectionError(
                "Bad connection to Redis."
            )
        return obj
