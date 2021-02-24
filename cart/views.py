from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = cart
    
    request.session['cart'] = cart
    return redirect(redirect_url)