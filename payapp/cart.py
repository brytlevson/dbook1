from mainapp.models import Product


class Cartitem():
    def __init__(self,book,amount):
        self.book = book
        self.amount = amount
        self.price_a= float(book.dangdang_price) * int(amount)


class Cart():
    def __init__(self):
        self.save_price=0
        self.total_price=0
        self.cartitem=[]

    # 用来计算购物车中商品的节省金额和总金额
    def sums(self):
        self.total_price=0
        self.save_price=0
        for i in self.cartitem:
            self.total_price+=float(i.book.dangdang_price)*int(i.amount)
            self.save_price+=(float(i.book.price)-float(i.book.dangdang_price))*int(i.amount)



    def add_book_toCart(self,bookid,amount):
        print(bookid,']]]]')
        for i in self.cartitem:
            if int(bookid)==i.book.id:
                i.amount=int(i.amount)+int(amount)
                self.sums()
                i.price_a=float(i.book.dangdang_price) * int(i.amount)
                # print(i.price,'单价和')
                return
        book = Product.objects.get(id=bookid)
        self.cartitem.append(Cartitem(book,amount))
        self.sums()


    #修改购物车中商品的数量
    def modify_book_cart(self,bookid,amount):
        for i in self.cartitem:
            if i.book.id == int(bookid):
                i.amount=amount
                print(i.amount,"i,amount")
            self.sums()
            i.price_a = float(i.book.dangdang_price) * int(i.amount)



    def delete_book_cart(self,bookid):
        for i in self.cartitem:
            if i.book.id == int(bookid):
                print(self.cartitem)
                self.cartitem.remove(i)
                print(self.cartitem)
            self.sums()











