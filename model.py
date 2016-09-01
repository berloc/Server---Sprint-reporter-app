from peewee import *


class ConnectDatabase:

    def connect_database():
        with open('connect_str.txt', "r") as f:
            return f.readline().strip()

    connect_str = connect_database()
    db = PostgresqlDatabase(connect_str)


class BaseModel(Model):

    class Meta:
        database = ConnectDatabase.db


class UserStory(BaseModel):

    story_title = CharField(null=True)
    user_story = CharField(null=True)
    acceptance_criteria = CharField(null=True)
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()