from logging import Formatter, getLogger, StreamHandler, DEBUG, handlers
import math

class Logger():
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
            filename='../.sushiLog',
            maxBytes=math.inf,
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

    def error(self, msg, errmsg):
        self.logger.error(msg + ' [{}]'.format(errmsg))

    def critical(self, msg):
        self.logger.critical(msg)
