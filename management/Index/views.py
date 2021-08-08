from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Count
from django.db.models import Sum, Min, Max, Avg


# Create your views here.


def customers(request):
    total_customers = Customer.objects.count()
    customer = Customer.objects.all()
    customer = Customer.objects.order_by('name')

    customer_form = CustomerForm
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
    customer_form = customer_form
    context = {'customer': customer, 'total_customers': total_customers, 'customer_form': customer_form}
    return render(request, 'Index/customers.html', context)


def create_customer(request):
    customer_form = CustomerForm
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
    customer = customer_form
    # product1 = Product.objects.get(name="Crayfish")

    context = {'customer': customer}
    return render(request, 'Index/newcustomer.html', context)


def product(request):
    products = ProductForm
    if request.method == "POST":
        products = ProductForm(request.POST)
        if products.is_valid():
            products.save()
    items = products
    context = {'items': items}
    return render(request, 'Index/product.html', context)


def dashboard(request):
    transact = Transactions
    if request.method == "POST":
        transact = Transactions(request.POST)
        if transact.is_valid():
            transact.save()
    transact = transact
    total = DailySupply.objects.filter(product=2)
    tot = total.count()
    product = Transaction.objects.all()
    calculation = Transaction.objects.all()
    context = {'transact': transact, 'calculation': calculation,
               'product': product, 'tot': tot}
    return render(request, 'Index/dashboard.html', context)


def supply(request):
    daily_supply = Supply
    if request.method == 'POST':
        daily_supply = Supply(request.POST)
        if daily_supply.is_valid():
            daily_supply.save()
    return render(request, 'Index/supply.html', {'daily_supply': daily_supply})


def orderform(request):
    daily_order = OrderForm
    if request.method == "POST":
        daily_order = OrderForm(request.POST)
        if daily_order.is_valid():
            daily_order.save()
        c_order = daily_order
    return render(request, "Index/dailyorder.html", {'daily_order': daily_order})


def total_supply(request):
    total_product1 = Product.objects.get(name="Cameroon Pepper")
    total_product1 = total_product1.dailysupply_set.all()
    total_product1 = total_product1.aggregate(Total=Sum('quantity'))
    total_product2 = Product.objects.get(name="Crayfish")
    total_product2 = total_product2.dailysupply_set.all()
    total_product2 = total_product2.aggregate(Total=Sum('quantity'))
    total_product3 = Product.objects.get(name="Red Pepper")
    total_product3 = total_product3.dailysupply_set.all()
    total_product3 = total_product3.aggregate(Total=Sum('quantity'))
    total_supplies = DailySupply.objects.aggregate(Total=Sum('quantity'))
    red_pepper = Product.objects.get(name="Red Pepper")
    r_supply = red_pepper.dailysupply_set.all()
    camer_pepper = Product.objects.get(name="Cameroon Pepper")
    c_supply = camer_pepper.dailysupply_set.all()
    crayfish = Product.objects.get(name="Crayfish")
    crayfish_supply = crayfish.dailysupply_set.all()
    total_crayfish = crayfish_supply.count()
    date = Product.objects.get(name="Crayfish")
    date1 = date.dailysupply_set.all()
    all_product = zip(c_supply, r_supply, crayfish_supply, date1)

    context = {'product': all_product, 'total_crayfish': total_crayfish, 'total': total_product3,
               'total_supplies': total_supplies, 'total1': total_product1, 'total2': total_product2}
    return render(request, 'Index/total.html', context)


def daily_order(request):
    return render(request, 'Index/_daily_order.html')