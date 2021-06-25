from abc import ABCMeta, abstractmethod
from typing_extensions import final
import sys
sys.path.append('../')

from framework.factory import Factory
from framework.product import Product
from .id_card import IDCard


class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []
    
        
    def _createProduct(self, owner):
        return IDCard(owner)
    
    def _registerProduct(self, product):
        return self.__owners.append(product.get_owner())
