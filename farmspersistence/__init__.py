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
