import logging
import re

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
        match = re.search(r'error_code=(\w+), module_name=([\w\s]+),', str(args))
        if match:
            self.error_code = match.group(1)
            self.module_name = match.group(2)
        else:
            self.error_code = ''
            self.module_name = ''

        super().__init__(*args, **kwargs)

logging.setLogRecordFactory(CustomLogRecord)