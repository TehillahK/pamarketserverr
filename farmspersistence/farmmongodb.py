import pymongo

from farmspersistence.farmdatabase import FarmDatabase


class FarmMongoDB(FarmDatabase):

    def __int__(self):
        self.url = ""
        self.db = None
        self.database_name = ""
        self.collection_name = ""
        self.collection = None

    def connect_db(self):
        try:
            my_client = pymongo.MongoClient(self.url)
            mydb = my_client[self.database_name]
            # self.collection = mydb[self.collection_name]
            self.collection = mydb[self.collection_name]
        except Exception as e:
            print("failed to connect")

    def get_all_farms(self):
        result = self.collection.find()
        return result

    def get_farm(self, farm_id):
        my_query = {"_id": id}
        farm = self.collection.find(my_query)
        return farm

    def get_farm_crops(self, farm_id):
        my_query = {"_id": id}
        farm = self.collection.find(my_query)
        return farm["crops"]
