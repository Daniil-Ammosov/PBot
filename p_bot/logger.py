import logging
from logging.handlers import RotatingFileHandler
import sys

__author__ = "Daniil Ammosov"


LOG_FILE = "/var/log/p_bot/log"

DICT_LOG_LVL = {
    "debug":    logging.DEBUG,
    "info":     logging.INFO,
    "warning":  logging.WARNING,
    "error":    logging.ERROR
}

LOGGER_NAME = "p_bot"


def get_logger(name=LOGGER_NAME, log_level="info"):
    message_format = u"%(asctime)s |%(levelname)5s |%(name)s | %(funcName)s |\nMESSAGE: %(message)s"
    datetime_format = u"[%d.%m.%Y %H:%M:%S]"
    formatter = logging.Formatter(fmt=message_format, datefmt=datetime_format)

    filehandler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=1024 * 1024 * 10,
        backupCount=5,
        encoding="utf-8"
    )
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)
    filehandler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(DICT_LOG_LVL.get(log_level, logging.INFO))
    logger.addHandler(filehandler)
    logger.addHandler(stream_handler)

    return logger


def set_log_lvl(log_level, name=LOGGER_NAME):
    logging.getLogger(name).setLevel(DICT_LOG_LVL.get(log_level, logging.INFO))
