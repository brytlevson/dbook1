import json

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Adang_project.settings")
django.setup()


from mainapp.models import Product, Category
from redis import Redis

red = Redis(host='192.168.111.128', port=7000)

# red.set("name", "Mr_lee")
# red.set("age", 18)
#
# age = red.get("age")
# print(age)
#
# red.lpush("hobby1", "football", "basketball")
# hobby = red.lrange("hobby1", 0, -1)
# print(hobby)



def mydefault(u):
    if isinstance(u,product):
        return {"id":u.id,"name":u.name,"paernt_id":u.parent_id}



product= list(Category.objects.all().values())
# print(product)
print(type(product))

user_dump = json.dumps(product,default=mydefault)


# print(user_dump)
# print(type(user_dump))
#
#
red.set('userlist',user_dump)

s=red.get("userlist")
print(s)
print(type(s))
results = json.loads(s.decode("utf-8"))
print(type(results))
print(results)

















