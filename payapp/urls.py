from django.contrib import admin
from django.urls import path, include
from payapp import views
from django.conf.urls import url
app_name = "payapp"
urlpatterns = [
    path('car/',views.car,name='car'),
    path('addcar/',views.addcar,name='addcar'),
    path('delete_cart/',views.delete_cart,name='delete_cart'),
    path('update_cart/',views.update_cart,name='update_cart'),
    url(r'^page1/(?P<money>.*)/', views.page1,name='page1'),
    path('pay/', views.pay,name='pay'),
    path('page2/',views.page2,name='page2'),
    path('paylogic/',views.paylogic,name='paylogic'),
    path('indent_ok/',views.indent_ok,name='indent_ok'),
]