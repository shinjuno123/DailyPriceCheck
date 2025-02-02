from django.contrib import admin
from .models import Product, Seller

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['id'] 
    list_display = ['sku', 'product_name']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    ordering = ['id'] 
    list_display = ['seller']  
