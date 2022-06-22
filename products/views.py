from . import forms
from django.shortcuts import render
from . import models
# Create your views here.


def product(request, product_id):
    product = models.Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'products/product.html', locals())
