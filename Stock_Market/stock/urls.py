
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('signup',views.SignUpAPI,name='Signup'),
    path('login/',views.LoginAPI,name='Login'),
    path('logout',views.logoutApi,name='Logout'),
    path('stock',views.product_add,name='Stock'),
    path('detail/',views.product_detail,name='Detail'),
    path('<int:id>',views.product_details,name='Details'),
    path('add',views.busy_stock,name='Buy'),
    path('ord',views.order_detail),
    path('contact',views.contect,name='contact')

]