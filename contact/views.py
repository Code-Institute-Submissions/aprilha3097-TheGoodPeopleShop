from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            content = request.POST.get('content')
            try:
                send_mail(
                    # to capture the user email it's displayd in subject field and can be responded to
                    f"Message from {contact_name}, <{contact_email}>",
                    content,
                    contact_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_success')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    context = {
        'form': form_class,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):

    return render(request, 'contact/contact_success.html')
