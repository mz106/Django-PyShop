
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
def index (request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new_products (request):
    return HttpResponse('New Products')
