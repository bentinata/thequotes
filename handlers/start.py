from telegram.ext import run_async


@run_async
def handler_start(bot, update, args):
    if update.effective_chat.type == "private":
        update.effective_message.reply_text("i will show help")
