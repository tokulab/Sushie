# from logging import Formatter, getLogger, StreamHandler, DEBUG
# import logging
#
# logger = getLogger('logtest')
# logger.setLevel(DEBUG)
#
# stream_handler = StreamHandler()
# stream_handler.setLevel(DEBUG)
# handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# stream_handler.setFormatter(handler_format)
#
# logger.addHandler(stream_handler)
#
# logger.debug('あ')

from logging import Formatter, getLogger, StreamHandler, DEBUG, handlers

class Logger:
    def __init__(self, n=__name__):
        self.logger = getLogger(n)
        self.logger.setLevel(DEBUG)
        formatt = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

        handler = handlers.RotatingFileHandler(
            filename='.SushiLog.log',
            maxBytes=2000,
            backupCount=5
        )
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
