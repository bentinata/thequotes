from models import Quote


def handler_add_quote(update, context):
    if update.effective_chat.type != 'private':
        message = update.effective_message
        chat = update.effective_chat
        if chat and message.reply_to_message:
            forwarded = message.reply_to_message.forward(-355145151)
            quote = Quote.create(
                chat_id=chat.id,
                user_id=message.reply_to_message.user.id,
                message_id=message.reply_to_message.message_id,
                stored_message_id=forwarded.message_id,
            )
            update.message.reply_text(
                f'Quote added! use ```/get {quote.id}``` to get the quote.'
            )
