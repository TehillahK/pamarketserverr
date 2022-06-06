import pymongo

from farmspersistence.farmdatabase import FarmDatabase
from bson.json_util import dumps
from bson.objectid import ObjectId


class FarmMongoDB(FarmDatabase):

    def __int__(self):
        self.url = "mongodb://localhost:27017/"
        self.db = None
        self.database_name = "pamarketfarms"
        self.collection_name = "lusaka"
        self.collection = None

    def connect_db(self):
        try:
            my_client = pymongo.MongoClient(self.url)
            mydb = my_client[self.database_name]
            # self.collection = mydb[self.collection_name]
            mydb[self.collection_name]
        except Exception as e:
            print("failed to connect")

    def get_all_farms(self):
        my_client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = my_client["pamarketfarms"]
        # self.collection = mydb[self.collection_name]
        result = list(mydb["lusaka"].find())
        result = dumps(result)
        return result

    def get_farm(self, farm_id, city="lusaka"):
        farm_id = ObjectId(farm_id)
        my_query = {"_id": farm_id}
        my_client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = my_client["pamarketfarms"]
        col = mydb[city]
        farm = col.find(my_query)
        result = dumps(farm[0])
        return result

    def get_farm_crops(self, farm_id):
        my_query = {"_id": id}
        farm = self.collection.find(my_query)
        return farm["crops"]
