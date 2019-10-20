from models import Quote


def handler_remove_quote(update, context):
    if str(context.args[0]).isdigit():
        quote_id = int(context.args[0])
        Quote.delete().where(Quote.id == quote_id)
        update.message.reply_text(f'Quote with id {quote_id} removed.')
    else:
        update.message.reply_text(f'Invalid quote id.')
