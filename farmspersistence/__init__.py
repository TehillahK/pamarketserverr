import json


# using depdency injection to pass in the database we are using
# this class gets farm data
class FarmsPersistence:
    def __init__(self, farmdb):
        self._db = farmdb

    def get_farm(self, farm_id):
        return self._db.get_farm(farm_id)

    def get_all_farms(self):
        return self._db.get_all_farms()

    def get_crops(self, farm_id):
        return self._db.get_farm_crops(farm_id)


class UsersPersistence:
    def __init__(self, userdb):
        self._db = userdb

    def get_user(self, email):
        return self._db.get_user(email)

    def add_user(self, email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0):
        return self._db.add_user( email, house_num, street_name, area, city, province, x_coordinate,y_coordinate)

    def get_all_users(self):
        return self._db.get_all_users()
