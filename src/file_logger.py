import os
import logging
from datetime import datetime
from src.loggers.base_logger import BaseLogger


class FileLogger(BaseLogger):
    def create_handler(self):
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        return logging.FileHandler(log_file)
