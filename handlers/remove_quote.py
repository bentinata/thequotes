from models import Quote


def handler_remove_quote(update, context):
    if str(context.args[0]).isdigit():
        chat = update.effective_chat
        quote_id = int(context.args[0])
        query = Quote.delete().where((Quote.id == quote_id) | (Quote.chat_id == chat.id))
        query.execute()
        update.message.reply_text(f'Quote with id {quote_id} removed.')
    else:
        update.message.reply_text(f'Invalid quote id.')
