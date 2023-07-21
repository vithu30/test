import logging


def set_logger_config(logger: logging, is_debug_enabled: bool = False):
    print(is_debug_enabled)
    logger_class = logger.getLogger()
    if is_debug_enabled:
        log_level = logger.DEBUG
    else:
        log_level = logger.INFO
    if len(logger.getLogger().handlers) > 0:
        logger_class.setLevel(log_level)
        logger_class.handlers[0].setFormatter(
            logger.Formatter(
                "%(asctime)s %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
            )
        )
    else:
        logger.basicConfig(
            level=log_level,
            format="%(asctime)s %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
        )
    return logger_class
