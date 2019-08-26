from django.contrib import admin
from django.urls import path, include



from mainapp import views
app_name = "mainapp"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/',views.detail,name="detail"),
    path('booklist/',views.booklist,name='booklist'),
    path('slurdetail/',views.slurdetail,name='slurdetail'),
    path('del2/',views.del2,name='del2'),
]