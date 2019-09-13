from logging import Formatter, getLogger, StreamHandler, DEBUG, handlers
import math

class Logger():
    def __init__(self, n=__name__):
        self.logger = getLogger(n)
        self.logger.setLevel(DEBUG)
        formatt = Formatter('%(asctime)s %(levelname)s - %(message)s')

        #stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

        handler = handlers.RotatingFileHandler(
            filename='.sushiLog',
            maxBytes=math.inf, # どのアルファベットで間違えたかの研究のため現状無制限にしてある
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

    def catch_ending(self):
        """
        :return: boolean
        """
        with open('.sushiLog', 'r') as log:
            latest_log = log.readlines()[-1].strip()
        # リザルト画面のocr結果がコレになるからそこで終わる
        exit_judge = True if 'HOA-FATH' in latest_log else False
        return exit_judge
