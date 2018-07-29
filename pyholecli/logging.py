import logging


def setupLogger(log_format):
    logging.root.handlers = []
    logging.basicConfig(format=log_format)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


LOG_FORMAT = '%(message)s'
logger = setupLogger(LOG_FORMAT)
