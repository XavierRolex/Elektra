from django import forms
from .models import Product
from category.models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'price', 'image', 'stock', 'is_available', 'category']