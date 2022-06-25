import pymongo

from farmspersistence.farmdatabase import FarmDatabase
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os


class FarmMongoDB(FarmDatabase):

    def __int__(self):

        load_dotenv()
        my_id = os.getenv("MONGO_URL")
        self.url = my_id
        self.db = None
        self.database_name = "farms"
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
        my_client = pymongo.MongoClient("mongodb+srv://doadmin:12p043lA9fa67PYc@pa-market-db-044f19b3.mongo.ondigitalocean.com/farms?tls=true&authSource=admin&replicaSet=pa-market-db")
        mydb = my_client["farms"]
        # self.collection = mydb[self.collection_name]
        result = list(mydb["lusaka"].find())
        result = dumps(result)
        return result

    def get_farm(self, farm_id, city="lusaka"):
        farm_id = ObjectId(farm_id)
        my_query = {"_id": farm_id}
        my_client = pymongo.MongoClient("mongodb+srv://doadmin:12p043lA9fa67PYc@pa-market-db-044f19b3.mongo.ondigitalocean.com/farms?tls=true&authSource=admin&replicaSet=pa-market-db")
        mydb = my_client["farms"]
        col = mydb[city]
        farm = col.find(my_query)
        result = dumps(farm[0])
        return result

    def get_farm_crops(self, farm_id):
        my_query = {"_id": id}
        farm = self.collection.find(my_query)
        return farm["crops"]
