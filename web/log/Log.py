#!python3
#encoding:utf-8
import logging
"""
class Log:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(handler)
        
    @property
    def Logger(self):
        return self.__logger
"""
def Singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@Singleton
class Log(object):
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(handler)
        
    @property
    def Logger(self):
        return self.__logger


if __name__ == '__main__':
    l = Log()
    l.Logger.setLevel(logging.DEBUG)
    l.Logger.debug('testですよ。')
    Log().Logger.debug('test2ですよ。')
