import logging


def handler_error(update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))
