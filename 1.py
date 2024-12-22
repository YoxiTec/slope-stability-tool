"""
COMP CS 100 Introduction to Programming
Student ID : 152687054
Name : Yohan Perera
Email: yohan.perera@tuni.fi
This is the program number 2 as practice for the exam
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self,name,price,sale=0):
        self.__name=name
        self.__price=price
        self.__sale=sale

    def printout(self):
        print(f"{self.__name}")
        print(f"  price: ",self.__price)
        print(f"  sale%:",self.__sale)

    def set_sale_percentage(self,sale_percentage):
        self.__sale=sale_percentage

    def get_price(self):
        modified_price=self.__price*(1-0.01*self.__sale)
        return modified_price

def main():
    test_products={
        "milk": 1.00,
        "sushi": 12.95
    }
    for product_name in test_products:
        print("="*20)
        print(f"TESTING: {product_name}")
        print("="*20)

        prod=Product(product_name,test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")
        print("-"*20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")
        print("-"*20)

        prod.set_sale_percentage(20.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")
        print("-"*20)


if __name__=="__main__":
    main()