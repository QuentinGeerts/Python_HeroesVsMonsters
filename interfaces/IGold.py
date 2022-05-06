from abc import ABC, abstractmethod

class IGold(ABC):

    @abstractmethod
    def gold(self):
        pass