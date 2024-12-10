from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="shopHome"),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('productView/<int:myid>', views.productView, name="productView"),
    path('checkout/', views.checkout, name="checkout"),
]