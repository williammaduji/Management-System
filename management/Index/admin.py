from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(DailyOrder)
admin.site.register(DailySupply)
admin.site.register(Transaction)
