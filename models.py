from peewee import *
import os

db = MySQLDatabase(
    "mpDB",
    user = os.environ["USER"],
    password = os.environ["PSWD"],
    host = "localhost",
    port = 3306
    )

class BaseModel(Model):
    class Meta:
        database = db

class Activities(BaseModel):
    id = AutoField(primary_key = True)
    bid = IntegerField()
    time = DateTimeField()
    activity = IntegerField()
    temp = FloatField()
    user = CharField()