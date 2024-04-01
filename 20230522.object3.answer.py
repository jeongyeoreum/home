class Product:
    discount_rate: float = 0.0

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return int(self.__price * (1 - self.discount_rate) * self.__quantity)

    def __str__(self):
        return f'{self.__name:30s}\t{self.__quantity:8d}개\t{self.__price:8,d}원'

    @classmethod
    def get_discount_rate(cls):
        return cls.discount_rate

    @classmethod
    def set_discount_rate(cls, rate):
        cls.discount_rate = rate


class Sales_Product(Product):
    discount_rate: float = 0.2

    @classmethod
    def get_discount_rate(cls):
        return cls.discount_rate

    @classmethod
    def set_discount_rate(cls, rate):
        cls.discount_rate = rate


class Clearance_Product(Product):
    discount_rate: float = 0.5

    # def get_price(self):
    #   super().get_price()
    #  return self.__price * (1-Clearance_Product.discount_rate) * self.__quantity

    @classmethod
    def get_discount_rate(cls):
        return cls.discount_rate

    @classmethod
    def set_discount_rate(cls, rate):
        cls.discount_rate = rate


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    def shop_list(self):
        return self.__shop_list

    def add(self, pdt):
        self.__shop_list.append(pdt)

    def delete(self, pdt, qty):
        updated = False
        for p in self.__shop_list:
            if p.name == pdt.name:
                p.quantity -= qty
                updated = True
                if p.quantity <= 0:
                    self.__shop_list.remove(p)
                break
        return updated

    def total_price(self):
        sum = 0
        for p in self.__shop_list:
            sum += p.get_price()

        return sum

    def billing(self):
        print('구입품목 :')
        print(f'{"품목명":38s}{"수량":10s}{"정상가":10s}{"할인가":10s}')

        for p in self.__shop_list:
            print(f'{p}\t{p.get_price():10,d}원')

        print(f'{58 * "-"}')
        print(f'{"합계":58s}{self.total_price()}원')

    def __str__(self):
        shop = ''
        for p in self.__shop_list:
            shop += f'{p}\n'
        return shop


if __name__ == '__main__':

    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Sales_Product('CJ햇반(210g*12입)', 13980, 1),
                Clearance_Product('노스페이스 올라운드 폴로 NT7PN00B', 65000, 1)]

    my_cart = ShoppingCart()

    for p in products:
        my_cart.add(p)
    print(my_cart)

    Product.set_discount_rate = 0.1

    my_cart.billing()


