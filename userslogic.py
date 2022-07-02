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
        return self.db_interface.get_user(email)

    def add_user(self, email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0):
        return self.db_interface.add_user(email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0)
