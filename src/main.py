import time

from loggers.logger_factory import LoggerFactory

main_logger = LoggerFactory.get_logger('main')

while True:
    main_logger.info("Python app is logging to file.")
    time.sleep(2)
