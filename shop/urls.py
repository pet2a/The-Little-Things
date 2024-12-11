from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop/index/', views.index, name="shopHome"),
    path('login/', views.login_view, name='login'),
    path('', views.register, name='register'),
    path('shop/about/', views.about, name="about"),
    path('shop/contact/', views.contact, name="contact"),
    path('shop/tracker/', views.tracker, name="tracker"),
    path('shop/search/', views.search, name="search"),
    path('shop/productView/<int:myid>', views.productView, name="productView"),
    path('shop/checkout/', views.checkout, name="checkout"),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]