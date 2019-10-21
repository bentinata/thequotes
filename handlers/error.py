import logging


def handler_error(update, error):
    logging.warning(f'error raised: {error}')
