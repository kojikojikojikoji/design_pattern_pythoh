from idcard.id_card import IDCard
from idcard.id_card_factory import IDCardFactory
from framework.factory import Factory
from framework.product import Product

def main2():
    # pass
    factory = IDCardFactory()
    card1 = factory.create("人1")
    card2 = factory.create("人2")
    card3 = factory.create("人3")
    card1.use()
    card2.use()
    card3.use()
    
if __name__ == '__main__':
    main2()