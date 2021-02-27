from django.shortcuts import render, get_object_or_404

def index(request):
    """ A view to return the Index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the About page """

    return render(request, 'home/about.html')
