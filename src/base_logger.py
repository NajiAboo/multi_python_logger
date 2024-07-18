import logging


class BaseLogger:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = self.create_handler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
        )
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def create_handler(self):
        raise NotImplementedError("Subclass must implement this function ")

    def get_logger(self):
        return self.logger
