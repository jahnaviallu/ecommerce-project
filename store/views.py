from django.shortcuts import render
from .models import Product,Category
from django.core.paginator import Paginator

def index(request):
    prods = Product.objects.all()

    return render(request,'index.html', {'prods' : prods})


def shop(request):
    prods = Product.objects.all()
    paginator = Paginator(prods, 6)
    
    page = request.GET.get('page')
    prods = paginator.get_page(page) #data
    return render(request, 'shop.html', {'prods' : prods})