class Product :
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self, price):
        return self.price * self.quantity  #리턴은 반환한다는 것. 프린트를 쓰지말고 리턴을 쓰자


    def __str__(self):
        return f'{self.name} {self.price}원 {self.quantity}개'  #>차지하는 칸수 지정하는 방법 :.3f 등 찾아서 복습하기





class ShoppingCart :
    def __init__(self):
        self.shop_list = []
        # shop_list에 제품 단가 수량을 한번에 저장하고 싶다  > 리스트 형태로 main 아래에 저장하면 된다.


    def add(self, pdt):
        self.shop_list.append(pdt)


    def delete(self, pdt, qty)->None:
        self.delete(pdt)
        d =self.shop_list.qty
        if d ==0 :
            return None



    def total_price(self)->int:
        sum = 0
        for p in self.shop_list:
            sum += p.get_price()

        return sum



    #실패작#def billing(self)->str:
        #return self.name + self.quantity + self.total_price
    def billing(self):
        print({self.shop_list} + {self.total_price()})



    def __str__(self):
        info = f'합계:{self.total_price:10s}  '

        #for p in self.shop_list:
         #   info += f'{product}\n'

        return info





if __name__ == '__main__':


    shoppingcart = [Product('제주 삼다수 그린 2L','1,200','5'), Product('신라면(120g*5입)','4,100','2')
     ,Product('CJ햇반(210g*12입)','13,980','1'), Product('몽쉘크림(12입)','4,780','1')]

    for p in shoppingcart:
      print(p)

    shoppingcart.add(Product('해태 구운감자(135g*5입)','3,580원','2개'))

    print(self.shop_list)

    total_price = 0
    for product in shoppingcart:
       # print(product.price)
        total_price += product.price
        print(total_price)


    #p = ShoppingCart('bill')
    #shoppingcart.biiling(shoppingcart)
    print(shoppingcart)


   # print(shoppingcart)




    #shoppingcart.delate('몽쉘크림(12입)')  # 쇼핑카트에 담긴 몽쉘크림 12입을 지우고 싶다

    #bill=billing(Product)  product를 billing한 결과를 bill에 저장하고 싶다,,
    #bill.add(shop_list)





    n = Product('해태 구운감자(135g*5입)','3,580원','2개')
    shoppingcart.add(n)
    print(shoppingcart)



    #shoppingcart.billing(shoppingcart)


