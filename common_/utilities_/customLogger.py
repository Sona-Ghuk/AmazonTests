import logging
from datetime import date
import os
from pathlib import Path

class AmazonTestEnvironment:
    def __init__(self, logger_name, log_file_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        logs_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_logs_')
        if not os.path.exists(logs_directory):
            os.makedirs(logs_directory)

        log_file = os.path.join(logs_directory, log_file_name)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


amazon_test_environment = AmazonTestEnvironment('test_logger', 'test.log')
logger = amazon_test_environment.get_logger()

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')