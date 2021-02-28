from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    """ Quantity will always be 1, product availability not implemented in project """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    """ Once in the view we grab the cart variable if it exists in the session
    or create it if it does not """
    cart = request.session.get('cart', {})

    """ If item is already in cart - do not add and redirect with error message """
    if item_id in list(cart.keys()):
        messages.error(request, f'{product.name} already in your cart! Check your cart to continue booking.')
        return redirect(redirect_url)
    else:
        """ If user attemptys to add more than 1 on the item quantity, error and redirect """
        if quantity > 1:
            messages.error(request, 'You can only add 1 item to your cart.')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


""" Remove an item in the shopping cart view """


def remove_from_cart(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
