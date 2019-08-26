from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import string
import random
from captcha.image import ImageCaptcha

from log_regapp.models import User


def login(request):
    return render(request,'log_regapp/login.html')



def check_user(request):
    name = request.GET.get("username")
    pwd = request.GET.get("userpwd")
    print("*******=======*************")
    result = User.objects.filter(email=name, password=pwd)
    if result:
        request.session['who']=result[0].nickname
        request.session['status'] = '1'
        return HttpResponse('0')
    return HttpResponse("1")

def checkcap(request):
    captcha = request.GET.get("captcha")
    # print(captcha)#能拿到用户输入的验证码
    cod0 = request.session.get("code")
    print("cod0==", cod0)
    if captcha.lower() == cod0.lower():
        return HttpResponse("1")
    return HttpResponse("0")









def regist(requet):
    return render(requet,'log_regapp/regist.html')




def registlogic(request):
    tel=request.POST.get('phone')
    request.session['tel']=tel
    nickname=request.POST.get('nickname')
    password=request.POST.get('txt_password')
    User.objects.create(email=tel,nickname=nickname,password=password,status=1)
    request.session['who']=nickname
    request.session['status']='1'
    return redirect('log_regapp:regist_ok')

def regist_ok(request):
    t=request.session.get('tel')
    n=request.session.get('who')
    del request.session['tel']
    print(t)
    return render(request,'log_regapp/regist_ok.html',{'T':t,'N':n})













# ajax验证注册号码是否已经存在
def check(request):
    name = request.GET.get("username")
    print(name, "====================")  # 能接收到

    result = User.objects.filter(email=name)  # 在数据库中比对
    print(result, "result")
    if result:
        # return HttpResponse("right_3.jpg")
        return HttpResponse("0")  # 存在是0
    if name:
        return HttpResponse("1")  # 通过是1
    return HttpResponse("0")




# 生成验证码

def getcaptcha(request):
    image = ImageCaptcha()  # 构造一个Image对象
    code = random.sample(string.ascii_letters + string.digits, 5)  # 随机产生5个随机数
    code = "".join(code)
    print(code)
    request.session["code"] = code  # 存储验证码
    data = image.generate(code)
    print(data)
    return HttpResponse(data, "image/png")






def indent(request):
    return render(request,'log_regapp/indent.html')



def order_info(request):
    name=request.POST.get('receive_people')
    print(name)
    address=request.POST.get('position')
    post_code=request.POST.get('post_code')
    tel=request.POST.get('tel')
    cart=request.session.get('cart')
    print(name,address,post_code,tel)
    return redirect('payapp:page1', cart.total_price)























