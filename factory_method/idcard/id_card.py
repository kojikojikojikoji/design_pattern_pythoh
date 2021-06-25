from abc import ABCMeta, abstractmethod
from typing_extensions import final
from framework.product import Product

 
class IDCard(Product):
    def __init__(self, owner):
        print(owner + "のカードを作ります")
        self.__owner = owner
        
    def use(self):
        print(self.__owner + "のカードを使います")
        
    def get_owner(self):
        return self.__owner
    
        
    