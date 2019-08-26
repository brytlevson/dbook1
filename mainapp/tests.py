from django.test import TestCase

# Create your tests here.



import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Adang_project.settings")
django.setup()

from mainapp.models import *


cate=Category.objects.get(id=18)

Product.objects.create(name="javas",author="李",face='static/images/1200x65_sk_1229.jpg',publishing_house='百知',edition=3,publishing_time="2003-5-7",print_time=5,isbn=0,word='1000',number_of_page=45,format_of_book='20',paper='16',emboitement='精装',sales='30',price=88,dangdang_price=38,review=60,issue='2013-4-2',score=8.6,sold_out='0',recommand='1',menus=cate,extend=0)

















