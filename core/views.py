from django.shortcuts import render, redirect
from django.contrib import messages
from product.models import Product

# Create your views here.

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    context = {
        'newest_products': newest_products,
    }
    return render(request, 'core/frontpage.html', context)


def contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and subject and message:
            # In production, you would send an email here
            # For now, we'll just show a success message
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
            return redirect('core:contact')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'core/contact.html')