import json

import pymongo
from bson.json_util import dumps
from dotenv import load_dotenv
import os
from farmspersistence.userdatabase import UserDatabase

load_dotenv()
url = os.getenv("MONGO_URL")


class UsersMongoDB(UserDatabase):

    def get_all_users(self):
        my_client = pymongo.MongoClient(url)
        mydb = my_client["users"]
        my_col = mydb["customers"]
        result = list(my_col.find())
        result = dumps(result)
        #print(result)
        return result

    def delete_user(self, email):
        try:
            my_client = pymongo.MongoClient(url)
            mydb = my_client["users"]
            my_col = mydb["customers"]
            myquery = {"email": email}
            my_col.delete_one(myquery)
        except pymongo.errors.ConnectionFailure:
            print("failed to get user")
            result = None
        except Exception as e:
            result = None
            print("failed")
            print(e)
        return result

    def get_user(self, email):
        try:
            my_query = {"email": email}
            my_client = pymongo.MongoClient(url)
            mydb = my_client["users"]
            col = mydb["customers"]
            user = col.find(my_query).limit(1)
            result = dumps(user[0])
            result = json.loads(result)
            result["message"] = "success"
            result = json.dumps(result)
            my_client.close()
        except pymongo.errors.ConnectionFailure:
            print("failed to get user")
            result = None
        except Exception as e:
            result = None
            print("failed")
            print(e)
        return result

    def add_user(self, email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0):
        try:
            my_client = pymongo.MongoClient(url)
            mydb = my_client["users"]
            col = mydb["customers"]
            mydict = {"email": email,
                      "address":
                          [
                            {
                             "houseNum": house_num,
                              "streetName": street_name,
                              "area": area,
                              "city": city,
                              "province": province,
                              "coordinates": [],
                            }
                          ]
                      }
            col.insert_one(mydict)
            result = {"success": True}
            result = json.dumps(result)
        except pymongo.errors.ConnectionFailure:
            print("failed to get user")
            result = None
        except Exception as e:
            result = None
            print("failed")
            print(e)
        return result
