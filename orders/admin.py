from django.contrib import admin

from . models import *

# Register your models here.
admin.site.register(Order2)
admin.site.register( OrderDetails)
admin.site.register(Payment)
