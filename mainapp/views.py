from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from mainapp.models import Category, Product


def index(request):
    w=request.session.get('who')
    if not w:
        w = ''
    flag = request.session.get('flag')
    cart = request.session.get("cart")
    if flag:
        return render(request, 'log_regapp/indent.html', {"cart": cart})

    cate=Category.objects.all().values()
    prod=Product.objects.filter(id__lt=9).values()
    return render(request,'mainapp/index.html',{"cate":cate,"prod":prod,"W":w})

def detail(request):
    ID=request.GET.get('id')
    p_detail=Product.objects.get(id=ID)
    return render(request,'mainapp/book_detail.html',{'p_d':p_detail})



def booklist(request):
    try:
        ID = request.GET.get('id')  # 拿到大类id
        print(ID)  # 1~7
        b = Category.objects.get(id=ID)  # 大类信息
        l1 = []
        l = Category.objects.filter(parent_id=ID)  # 自己的二类category
        for i in l:
            print(i.name, i.product_set.all().count())
            l1.append(i.id)
        print(l1)
        p = Product.objects.filter(menus__in=l1)  # 大类下的所有书籍
        print(p)
        for j in p:
            print(j.name, j.id)
        # 分页
        number = request.GET.get("page")  # 地址栏拼接获取 后面用  第一次为none
        if number is None:
            number = 1
        pagtor = Paginator(p, per_page=3)  # 分页器对象
        page = pagtor.page(number)  # 第2页  页面对象
        return render(request, 'mainapp/booklist.html', {"l": l, "B": b, "P": page})
    except:
        return HttpResponse("页面出现错误，请重新登录")



def slurdetail(request):
    ID=request.GET.get("id")   # 接收的是二级id

    d=Category.objects.get(id=ID) #拿到二级的信息
    # 查找二级id所属的大类
    b=Category.objects.get(id=d.parent_id) #大类信息
    #查找该大类下的所有二级分类
    l1=[]
    l = Category.objects.filter(parent_id=b.id)
    #需要展示的二类书籍
    for i in l:
        l1.append(i.id)
    p=Product.objects.filter(menus=ID) #需要显示的书籍信息
    # 分页
    number = request.GET.get("page")  # 地址栏拼接获取 后面用  第一次为none
    if number is None:
        number = 1
    pagtor = Paginator(p, per_page=3)  # 分页器对象
    page = pagtor.page(number)  # 第2页  页面对象
    return render(request, 'mainapp/slurdetail.html', {"l": l, "B": b, "P": page,"D":d})

def del2(request):
    try:
        del request.session['who']
    except:
        pass
    return HttpResponse("111111")









