from django.shortcuts import render
from shop.models import *
# Create your views here.



def home(request):

    products = Products.objects.all()
    ctx = {'products' : products}
    return render(request , 'shop/home.html' , ctx)
