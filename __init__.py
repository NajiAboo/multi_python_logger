import logging

from multi_python_logger import logger_instance as logger

def log_with_context(level, msg, module_name='', error_code='', *args, **kwargs):
    extra = {'module_name': module_name, 'error_code': error_code}
    logger.log(level, msg, *args, extra=extra, **kwargs)

def info(msg, module_name='', error_code='', *args, **kwargs):
    log_with_context(logging.INFO, msg, module_name, error_code, *args, **kwargs)

def error(msg, module_name='', error_code='', *args, **kwargs):
    log_with_context(logging.ERROR, msg, module_name, error_code, *args, **kwargs)