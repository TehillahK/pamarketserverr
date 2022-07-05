# Pa Market backend code starter
#  written by Tehillah Kangamba
# all database stuff is famerpersitance package
from farmspersistence import UsersPersistence
from farmspersistence.usersmongodb import UsersMongoDB


class UsersSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not UsersSingleton.__instance:
            UsersSingleton.__instance = object.__new__(cls)
        return UsersSingleton.__instance

    def __init__(self):
        db = UsersMongoDB()
        self.db_interface = UsersPersistence(db)

    def get_user(self,email):
        result = {}
       # print("here")
        req_farm = self.db_interface.get_user(email)
        if req_farm is None:
            #create farm
            self.db_interface.add_user(email,"","","","","")
            #print("create user")
        result = req_farm
        return result

    def update_user(self,query,new_vals):
        return self.db_interface.update_user(query,new_vals)

    def add_user(self, email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0):
        return self.db_interface.add_user(email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0)

    def get_all_users(self):
        return self.db_interface.get_all_users()
