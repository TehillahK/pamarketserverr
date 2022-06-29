import pymongo

from farmspersistence.farmdatabase import FarmDatabase
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("MONGO_URL")

class FarmMongoDB(FarmDatabase):

    def __int__(self):
        self.db = None
        self.database_name = "farms"
        self.collection_name = "lusaka"
        self.collection = None

    def connect_db(self):
        try:
            my_client = pymongo.MongoClient(url)
            mydb = my_client[self.database_name]
            # self.collection = mydb[self.collection_name]
            mydb[self.collection_name]
        except Exception as e:
            print("failed to connect")

    def get_all_farms(self):
        my_client = pymongo.MongoClient(url)
        mydb = my_client["farms"]
        # self.collection = mydb[self.collection_name]
        result = list(mydb["lusaka"].find())
        result = dumps(result)
        return result

    def get_farm(self, farm_id, city="lusaka"):
        farm_id = ObjectId(farm_id)
        my_query = {"_id": farm_id}
        my_client = pymongo.MongoClient(url)
        mydb = my_client["farms"]
        col = mydb[city]
        farm = col.find(my_query).limit(1)
        result = dumps(farm[0])
        return result

    def get_farm_crops(self, farm_id):
        my_query = {"_id": id}
        farm = self.collection.find(my_query)
        return farm["crops"]
