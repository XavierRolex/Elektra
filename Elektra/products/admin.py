from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'category', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available', 'category', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)