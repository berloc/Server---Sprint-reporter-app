from model import *


# db.connect()
ConnectDatabase.db.connect()
ConnectDatabase.db.drop_tables([UserStory], safe=True, cascade=True)
ConnectDatabase.db.create_tables([UserStory], safe=True)
