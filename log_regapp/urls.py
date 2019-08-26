from django.contrib import admin
from django.urls import path, include



from log_regapp import views
app_name = "log_regapp"
urlpatterns = [
    path('login/',views.login,name="login"),
    path('regist/',views.regist,name="regist"),
    path('registlogic/',views.registlogic,name="registlogic"),
    path('check/',views.check,name="check"),
    path('getcaptcha/',views.getcaptcha,name="getcaptcha"),
    path('regist_ok/',views.regist_ok,name="regist_ok"),
    path('check_user/',views.check_user,name="check_user"),
    path('checkcap/',views.checkcap,name="checkcap"),
    path('indent/',views.indent,name="indent"),
    path('order_info/',views.order_info,name="order_info"),
]