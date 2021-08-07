from django.db import models
import datetime
from django import forms


# Create your models here.

class DateInput(forms.DateInput):
    input_type = 'date'


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)
    phone_number = models.CharField(null=True, unique=True, blank=True, max_length=13)
    date_created = models.DateField(null=True, default=datetime.date.today)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, null=True, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    date_created = models.DateField(null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product


class Transaction(models.Model):
    title = models.CharField(max_length=20)
    total_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    debit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    paid = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.total_balance}{self.debit}{self.paid}"

    def debt(self):
        return self.debit + self.total_balance

    def credit(self):
        return self.total_balance - self.paid

    def balance(self):
        return self.total_balance


class DailySupply(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    date = (models.DateField(default=datetime.date.today))

    def __str__(self):
        return str(self.date)


class DailyOrder(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True, blank=True)
    money_received = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.date)
