from django import forms
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'date_created', 'email']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class Transactions(ModelForm):
    class Meta:
        model = Transaction
        fields = ['debit', 'total_balance', 'paid']


class Supply(ModelForm):
    class Meta:
        model = DailySupply
        fields = ['product', 'quantity', 'date']


class OrderForm(ModelForm):
    class Meta:
        model = DailyOrder
        fields = ['product', 'quantity', 'customer', 'money_received', 'date']


"""class TotalBalance(ModelForm):
    class Meta:
        model = Transactions
        fields = ['total_balance']


class Credit(ModelForm):
    class Meta:
        model = Transactions
        fields = ['paid']
"""
