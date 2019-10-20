from peewee import *

from models.base import BaseModel


class Quote(BaseModel):
    chat_id = IntegerField()
    user_id = IntegerField()
    message_id = IntegerField()
    stored_message_id = IntegerField()
