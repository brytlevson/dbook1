import json

from  payapp.cart import Cart
from django.http import HttpResponse
from django.shortcuts import render,redirect
from alipay import AliPay
import time
# Create your views here.

def car(request):
    cart = request.session.get('cart')
    w = request.session.get('who')
    if cart:
        for i in cart.cartitem:
            print(i.book.name, i.amount, i.price_a)
        return render(request, 'payapp/car.html', {"cart": cart, "W": w})
    else:
        return render(request, 'payapp/car.html')




# def addcar(request):
#     name=request.POST.get('bookid')
#     num=request.POST.get('booksum')
#     print(name,num)
#     return HttpResponse("成功")


def addcar(request):
    #搜集参数
    bookid = request.POST.get('bookid')
    num = int(request.POST.get('booknum'))
    cart = request.session.get('cart') #看之前的购物车
    print(bookid, num,'============')
    print(cart)
    if cart is None:
        cart =Cart() #创建购物车
        cart.add_book_toCart(bookid,num)
        #将购物车重新存储到session中
        request.session['cart']=cart #存购物车
    else:
        #购物车已经存在
        cart.add_book_toCart(bookid,num)
        request.session['cart'] = cart  # 重新存购物车
    print(bookid, num, '*******')
    # cart=request.session.get('cart')
    # for i in cart.cartitem:
    #     print(i.book.name,i.amount)
    return HttpResponse("成功加入到购物车")



def update_cart(request):
    #搜集参数
    bookid=request.POST.get('bookid')
    amount=request.POST.get('amount')
    print(bookid,"*******",amount)
    cart=request.session.get("cart")
    print(cart)

    #调用方法修改购物车
    cart.modify_book_cart(bookid,amount)
    #存session
    request.session['cart'] = cart
    #需要返回的数据
    d1={"t_money":cart.total_price,"s_money":cart.save_price}
    print(d1,"d1")
    str1 = json.dumps(d1)
    return HttpResponse(str1)

#
def delete_cart(request):
    #获取删除书籍的id
    bookid=request.POST.get('bookid')
    print("bookid",bookid)
    cart=request.session.get("cart")
    #调用方法
    cart.delete_book_cart(bookid)
    #存session
    request.session['cart'] = cart

    # 需要返回的数据
    d1 = {"t_money": cart.total_price, "s_money": cart.save_price}
    print(d1, "d1")
    str1 = json.dumps(d1)
    return HttpResponse(str1)



app_private_key_string = open("D:\百知资料\沙箱支付\RSA签名验签工具windows_V1.4\RSA密钥\应用私钥2048.txt").read()
alipay_public_key_string = open("D:\百知资料\沙箱支付\RSA签名验签工具windows_V1.4\RSA密钥\应用公钥2048.txt").read()
app_private_key_string == """
    -----BEGIN RSA PRIVATE KEY-----
    base64 encoded content
    -----END RSA PRIVATE KEY-----
"""

alipay_public_key_string == """
    -----BEGIN PUBLIC KEY-----
    base64 encoded content
    -----END PUBLIC KEY-----
"""

alipay1 = AliPay(
    appid="2016092700608457",
    app_notify_url=None,
    app_private_key_string=app_private_key_string,

    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA",
    debug=False
)




def pay(request):
    # return render(request,'payapp/index.html')
    return HttpResponse("111123")


def page1(request,money):
    # if request.method == "GET":
    #     return render(request, 'page1.html')
    # else:
    state=request.session.get("status")
    if state:
        print('付款金额', money)
        alipay = alipay1
        # 生成支付的url
        query_params = alipay.api_alipay_trade_page_pay(

            subject="123456",  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
            return_url='http://127.0.0.1:8000/payapp/indent_ok/?money='+money  # 可以设置跳转路径
        )

        pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)

        return redirect(pay_url)
    else:

        return render(request,'log_regapp/login.html')





def indent_ok(request):
    return render(request,'payapp/indent_ok.html')













def page2(request):
    alipay = alipay1
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('POST验证', status)
        return HttpResponse('POST返回')

    else:
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('GET验证', status)
        return HttpResponse('支付成功')





def paylogic(request):
    state=request.session.get('status')  #获取登录状态
    cart = request.session.get("cart")
    if state:
        return render(request,'log_regapp/indent.html',{"cart":cart})  # 填写收货信息
    else:
        request.session['flag'] = 1
        return render(request,'log_regapp/login.html')
















