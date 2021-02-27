from django.shortcuts import render, get_object_or_404

from .models import Charity
from .forms import CharityForm

def all_charities(request):
    """ View to view all products """
    charities = Charity.objects.all()

    context = {
        'charities': charities,
    }

    return render(request, 'charities/charities.html', context)

def charity_detail(request, charity_id):
    """ A view to show individual product details """
 
    charity = get_object_or_404(Charity, pk=charity_id)

    context = {
        'charity': charity,
    }

    return render(request, 'charity/charity_detail.html', context)

