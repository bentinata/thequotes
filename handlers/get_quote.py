from models import Quote


def handler_get_quote(update, context):
    if str(context.args[0]).isdigit():
        quote_id = int(context.args[0])
        if Quote.select().where(Quote.id == quote_id).exists():
            quote = Quote.get(Quote.id == quote_id)
            # TODO forward the quoted message
            update.message.reply_text(f'under construction {quote_id} {quote.stored_message_id}.')
            return
    update.message.reply_text(f'Invalid quote id.')
