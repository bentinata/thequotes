from peewee import fn

from models import Quote


def handler_get_random_quote(update, context):
    chat = update.effective_chat
    if Quote.select().where(Quote.chat_id == chat.id).count():
        selected_quote = Quote.select().where(Quote.chat_id == chat.id).order_by(fn.Random()).limit(1)[0]
        chat.bot.forward_message(
            chat_id=chat.id,
            from_chat_id=chat.id,
            message_id=selected_quote.stored_message_id
        )
        return
    update.message.reply_text('Please add at least one quote first.')
