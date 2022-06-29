import pymongo

from farmspersistence.farmdatabase import FarmDatabase
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

from farmspersistence.userdatabase import UserDatabase

load_dotenv()
url = os.getenv("MONGO_URL")


class UsersMongoDB(UserDatabase):

    def get_user(self, email):
        try:
            my_query = {"email": email}
            my_client = pymongo.MongoClient(url)
            mydb = my_client["users"]
            col = mydb["customers"]
            user = col.find(my_query)
            result = dumps(user[0])
        except pymongo.errors.ConnectionFailure:
            print("failed to get user")
            result = None
        except Exception as e:
            result=None
            print("failed")
            print(e)
        return result
