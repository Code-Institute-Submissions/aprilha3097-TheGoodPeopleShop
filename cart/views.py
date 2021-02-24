from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    """ Once in the view we grab the bag variable if it exists in the session
    or create it if it  does not """
    cart = request.session.get('cart', {})

    """ Then, we add the item to the cart or update the
    quantity if it already exists """
    if item_id in list(cart.keys()):
        messages.error(request, f'{product.name} already in your cart! Check your cart to continue booking.')
        return redirect(redirect_url)
    else:
        if quantity > 1:
            messages.error(request, 'You can only add 1 item to your cart.')
        else: 
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)