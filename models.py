from peewee import *
import os

db = MySQLDatabase(
    "mpDB",
    user = "mellaniem",
    password = "7minutes",
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
    treatment = CharField()
    exposure = BooleanField() # True for experimental exposure, False for observation

class Weights(BaseModel):
    id = AutoField(primary_key = True)
    user = CharField()
    bid = IntegerField()
    time = DateTimeField()
    treatment = CharField()
    weight_before = FloatField()
    weight_after = FloatField()