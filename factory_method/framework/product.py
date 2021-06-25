from abc import ABCMeta, abstractclassmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass