import logging


class BaseLogger:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = self.create_handler()
        # formatter = logging.Formatter(
        #     "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
        # )
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(module_name)s - %(error_code)s - %(levelname)s - %(message)s'
        )
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def create_handler(self):
        raise NotImplementedError("Subclass must implement this function ")

    def get_logger(self):
        return self.logger



class CustomLogRecord(logging.LogRecord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = kwargs.get('module_name', '')
        self.error_code = kwargs.get('error_code', '')

logging.setLogRecordFactory(CustomLogRecord)