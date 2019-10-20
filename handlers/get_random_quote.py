from peewee import fn

from models import Quote


def handler_get_random_quote(update, context):
    chat = update.effective_chat
    if Quote.select().where(Quote.chat_id == chat.id).count():
        selected_quote = Quote.select().where(Quote.chat_id == chat.id).order_by(fn.Random()).limit(1)
        # TODO forward the quoted message
        update.message.reply_text(f'under construction {selected_quote.stored_message_id}.')
        return
    update.message.reply_text('Please add at least one quote first.')
