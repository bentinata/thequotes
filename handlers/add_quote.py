from models import Quote


def handler_add_quote(update, context):
    if update.effective_chat.type != 'private':
        message = update.effective_message
        chat = update.effective_chat
        if chat and message.reply_to_message:
            forwarded = message.reply_to_message.forward(update.message.chat.id, disable_notification=True)
            quote = Quote.create(
                chat_id=chat.id,
                user_id=message.reply_to_message.from_user.id,
                message_id=message.reply_to_message.message_id,
                stored_message_id=forwarded.message_id,
            )
            update.message.reply_markdown(
                f'Quote added! use `/get {quote.id}` to get the quote and /remove {quote.id} to remove it.'
            )
