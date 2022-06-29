from abc import ABC, abstractmethod


class UserDatabase(ABC):
    @abstractmethod
    def get_user(self,email):
        pass
