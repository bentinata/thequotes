def handler_start(update, context):
    if update.effective_chat.type == 'private':
        update.message.reply_text('Henlo! add me to your group.')
