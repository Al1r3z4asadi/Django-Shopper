from django.contrib import admin
from django.urls import path , include
from shop import views as shop_views

urlpatterns = [
    path('' , shop_views.home , name='shopper-home'),
]
