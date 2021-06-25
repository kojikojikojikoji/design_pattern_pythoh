from abc import ABCMeta, abstractmethod
from typing_extensions import final

class Factory(metaclass=ABCMeta):
    @final
    def create(self, owner):
        p = self._createProduct(owner)
        self._registerProduct(p)
        return p
    
    @abstractmethod
    def _createProduct(self, owner):
        pass
    
    @abstractmethod
    def _registerProduct(self, owner):
        pass    