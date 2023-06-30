from utils.patterns.init_caller_meta import ConnectionCaller
from utils.patterns.singleton_meta import SingletonMeta


class SingletonConnectionMixinMeta(SingletonMeta, ConnectionCaller):
    """Return singleton obj and execute method 'try_connection'."""
    pass
