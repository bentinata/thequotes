import logging

from telegram.ext import Updater, CommandHandler

from handlers import handler_start
from handlers.add_quote import handler_add_quote
from handlers.get_quote import handler_get_quote
from handlers.get_random_quote import handler_get_random_quote
from handlers.remove_quote import handler_remove_quote


class Bot:

    def __init__(self, token, url, webhook_url, private_key, certificate, port, workers=4, debug=False):
        self._webhook_url = webhook_url
        self._token = token
        self._url = url
        self._port = port
        self._private_key = private_key
        self._certificate = certificate
        self._updater = Updater(token, workers=workers, use_context=True)
        self._init_handlers()

    def run(self):
        u = self._updater
        if self._certificate:
            u.start_webhook(
                listen=self._url,
                port=self._port,
                url_path=self._token,
                key=self._private_key,
                cert=self._certificate,
                webhook_url='{}:{}/{}'.format(self._webhook_url,
                                              self._port,
                                              self._token)
            )
        else:
            u.start_webhook(
                listen=self._url,
                port=self._port,
                url_path=self._token,
            )
            u.bot.set_webhook(
                '{}/{}'.format(
                    self._webhook_url,
                    self._token,
                )
            )
        logging.warning('Bot Running~')
        u.idle()

    def _init_handlers(self):
        start_handler = CommandHandler("start", handler_start, pass_args=True)
        add_quote_handler = CommandHandler("add", handler_add_quote)
        get_random_quote_handler = CommandHandler("random", handler_get_random_quote)
        get_quote_handler = CommandHandler("get", handler_get_quote, pass_args=True)
        remove_quote_handler = CommandHandler("remove", handler_remove_quote, pass_args=True)

        dp = self._updater.dispatcher
        dp.add_handler(start_handler)
        dp.add_handler(add_quote_handler)
        dp.add_handler(get_random_quote_handler)
        dp.add_handler(get_quote_handler)
        dp.add_handler(remove_quote_handler)
        # dp.add_error_handler(handler_error)
