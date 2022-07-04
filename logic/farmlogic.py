from farmspersistence import FarmsPersistence
from farmspersistence.fakefarmdb import FakeFarmDB


## From stack overflow
from farmspersistence.farmmongodb import FarmMongoDB


class FarmsSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not FarmsSingleton.__instance:
            FarmsSingleton.__instance = object.__new__(cls)
        return FarmsSingleton.__instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        db = FarmMongoDB()
        self.db_interface = FarmsPersistence(db)

    def get_all_farms(self):
        return self.db_interface.get_all_farms()

    def get_crops(self, farm_id):
        return self.db_interface.get_crops(farm_id)

    def get_farm(self,farm_id):
        return self.db_interface.get_farm(farm_id)
#############################################################################################

