import logging
import os
from logging.handlers import RotatingFileHandler


class LoggerFactory:
    _loggers = {}
    _logs_dir = "./logs"

    @staticmethod
    def get_logger(name: str,
                   level: int | str = logging.INFO,
                   file_name: str = "app.log",
                   max_bytes: int = 5_000_000,
                   backup_count: int = 5,
                   log_to_console: bool = False,
                   ) -> logging.Logger:
        logger_key = (name, level)
        if logger_key in LoggerFactory._loggers:
            return LoggerFactory._loggers[logger_key]

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = False

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        if log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        os.makedirs(LoggerFactory._logs_dir, exist_ok=True)
        log_file = os.path.join(LoggerFactory._logs_dir, file_name)
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        LoggerFactory._loggers[logger_key] = logger
        return logger
