from abc import ABC, abstractmethod


class UserDatabase(ABC):
    @abstractmethod
    def get_user(self, email):
        pass

    @abstractmethod
    def add_user(self, email, house_num, street_name, area, city, province, x_coordinate=0, y_coordinate=0):
        pass

    @abstractmethod
    def delete_user(self, email):
        pass

    @abstractmethod
    def get_all_users(self):
        pass
