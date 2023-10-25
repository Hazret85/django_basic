from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Product, Order


def shop_index(request):
    return render(request, 'shopapp/shop-index.html')


def product_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html',context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
