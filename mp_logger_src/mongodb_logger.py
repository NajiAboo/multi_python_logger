import logging
import motor.motor_asyncio
from mp_logger_src.base_logger import BaseLogger

class MongoDBLogger(BaseLogger):
    def __init__(self,config):
        super().__init__(config)
        self.client = motor.motor_asyncio.AsyncIOMotorClient(config['mongodb_uri'])
        self.db = self.client[config['mongodb_db']]
        self.collection = self.db[config['mongodb_collection']]

    def create_handler(self):
        return MongoDBHandler(self.collection)

class MongoDBHandler(logging.Handler):
    def __init__(self, collection):
        super().__init__()
        self.collection = collection

    def emit(self, record):
        log_entry = self.format(record)
        self.collection.insert_one(log_entry)

    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module_name": getattr(record, 'module_name', ''),
            "error_code": getattr(record, 'error_code', ''),
            "filename": record.pathname,
            "line_number": record.lineno,
            "function": record.funcName,
        }
        return log_entry

    def formatTime(self, record, datefmt=None):
        import time
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = "%s,%03d" % (t, record.msecs)
        return s
