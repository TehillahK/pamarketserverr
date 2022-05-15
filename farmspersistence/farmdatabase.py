from abc import ABC, abstractmethod


class FarmDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_farms(self):
        return None

    @abstractmethod
    def get_farm(self, farm_id):
        pass

    @abstractmethod
    def get_farm_crops(self, farm_id):
        pass
