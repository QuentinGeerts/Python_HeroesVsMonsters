from abc import ABC, abstractmethod

class IGold(ABC):

    @property
    @abstractmethod
    def gold(self):
        pass