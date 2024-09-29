import logging
import os

logger = logging.getLogger("inventory_logger")

logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'inventory_logs.log'))
console_handler = logging.StreamHandler()

verbose_formatter = logging.Formatter('%(levelname)s %(asctime)s %(name)s.%(module)s API Name: %(funcName)s %(message)s')
simple_formatter = logging.Formatter('%(levelname)s: %(message)s')

file_handler.setFormatter(verbose_formatter)
console_handler.setFormatter(simple_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)