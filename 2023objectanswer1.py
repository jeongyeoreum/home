
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price*self.quantity

    def __str__(self):
        return f'{self.name:30s}\t{self.price:5d}원{self.quantity:3d}개'


class ShoppingCart:
    def __init__(self):
        self.shop_list = []

    def add(self, pdt):
        self.shop_list.append(pdt)


    def delete(self, pdt, qty):
        updated = False
        for p in self.shop_list:
            if p.name == pdt.name:
                p.quantity -= qty
                updated = True
                if p.quantity <= 0:
                    self.shop_list.remove(p)
                break
        return  updated


    def total_price(self):
        sum = 0
        for p in self.shop_list:
            sum += p.get_price()

        return sum


    def billing(self):
        print ('구입품목')

        for p in self.shop_list:
            print(f'{p}\t{p.get_price():8d}원')
        print (f'{45*"-"}')
        print(f'{"합계":38s}{self.total_price():8d}원')


    def __str__(self):
        shop = ''
        for p in self.shop_list:
            shop += f'{p}\n'
        return shop


if __name__ == '__main__':

    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Product('CJ햇반(210g*12입)', 13980, 1),
                Product('몽쉘크림(12입)', 4780, 1)]

   # for product in products:
    #    print(f'{product}---> {product.get_price():6d}원')

    my_cart = ShoppingCart()

    for p in products:
        my_cart.add(p)

    print(my_cart)

    my_cart.billing()

    my_cart.delete(products[3], 1)
    my_cart.billing()

    my_cart.add(Product('해태 구운감자(135g*5입)', 3580, 2))
    my_cart.billing()

