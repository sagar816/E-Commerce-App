from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil(n/4) + (n//4)
        allProds.append([prod, range(1, nSlides), nSlides])


    #params = {'no_of_slides':nSlides, 'range': range(1, nSlides), 'product': products}
    #allProds = [[products, range(1, nSlides), nSlides],
     #           [products, range(1, nSlides), nSlides]
      #          ]
    params = {'allProds': allProds}
    return render(request, 'buy/index.html', params)

def about(request):
    return render(request, 'buy/about.html')

def contact(request):
    return render(request, 'buy/contact.html')

def tracker(request):
    return render(request, 'buy/tracker.html')

def search(request):
    return render(request, 'buy/search.html')

def productView(request, myid):
    #fetch the product using the id
    Product = product.objects.filter(id=myid)

    return render(request, 'buy/prodView.html', {'Product':Product[0]})

def checkout(request):
    return render(request, 'buy/checkout.html')