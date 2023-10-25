from django.urls import path
from .views import shop_index, product_list, orders_list

app_name = 'shopapp'

urlpatterns = [
    path('',shop_index,name='index'),
    path('products/',product_list,name='products_list'),
    path('orders/',orders_list,name = 'orders_list')
]
