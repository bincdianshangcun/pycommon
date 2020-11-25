import sys
import logging


def setup_logging(level=logging.INFO):
    if level is None:
        level = logging.INFO

    # time format: 2019-07-17 09:58:57,954
    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s %(process)d %(levelname)s %(message)s',
        level=level)
