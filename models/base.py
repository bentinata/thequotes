from datetime import datetime

from peewee import Model, DateTimeField

from database import db


class BaseModel(Model):
    created = DateTimeField(default=datetime.now)

    class Meta:
        database = db
