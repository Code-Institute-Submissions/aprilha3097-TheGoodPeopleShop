from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.


def all_products(request):
    
    products = Product.objects.all()

    return render(request, 'products/products.html')