from django.contrib import admin
from .models import Product, PurchaseOrder


class ProductsDetails(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'price', 'user']

class PurchaseOrderDetails(admin.ModelAdmin):

    list_display = ['id', 'product', 'user', 'price', 'buying_date']

admin.site.register(Product, ProductsDetails)
admin.site.register(PurchaseOrder, PurchaseOrderDetails)
