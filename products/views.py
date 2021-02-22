from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product

def all_products(request):
    """ View to view all products """
    products = Product.objects.all()
    
    return render(request, 'products/products.html', {'all_items': products})

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)