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
            '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
        )
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def create_handler(self):
        raise NotImplementedError("Subclass must implement this function ")

    def get_logger(self):
        return self.logger

    def log(self, log_type, msg, module_name='', error_code=''):
        formatted_msg = f"error_code={error_code}, module_name={module_name}, message={msg}"
        
        if log_type.lower() == 'info':
            self.logger.info(formatted_msg)
        elif log_type.lower() == 'error':
            self.logger.error(formatted_msg)
        else:
            self.logger.debug(formatted_msg)



class CustomLogRecord(logging.LogRecord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = kwargs.get('module_name', '')
        self.error_code = kwargs.get('error_code', '')

logging.setLogRecordFactory(CustomLogRecord)