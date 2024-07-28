from mp_logger_src import logger_instance

def log(log_type, msg, module_name='', error_code='', *args, **kwargs):
    formatted_msg = f"error_code={error_code}, module_name={module_name}, message={msg}"
    extra = {'module_name': module_name, 'error_code': error_code}

    if log_type.lower() == 'info':
        logger_instance.info(formatted_msg,  *args, **kwargs)
    elif log_type.lower() == 'error':
        logger_instance.error(formatted_msg, *args,  **kwargs)
    else:
        logger_instance.debug(formatted_msg, *args,  **kwargs)