from abc import ABC, abstractmethod


class ILeather (ABC):

    @property
    @abstractmethod
    def leather(self):
        pass
