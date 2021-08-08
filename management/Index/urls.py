from django.urls import path
from . import views


urlpatterns = [
    path('customers', views.customers, name='customers'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('daily_supply', views.supply, name='daily_supply'),
    path('total', views.total_supply, name='total'),
    path('daily_order_form', views.orderform, name='daily_order_form'),
    path('daily_order', views.daily_order, name='daily_order'),
    path('product', views.product, name='product')
]