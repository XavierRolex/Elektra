from django.shortcuts import render

def home(request):
    featured_products = [
        {"name": "Product 1", "description": "A great product", "price": 20, "image": "/static/product1.jpg"},
        {"name": "Product 2", "description": "Another great product", "price": 30, "image": "/static/product2.jpg"},
    ]
    return render(request, 'store/home.html', {"featured_products": featured_products})
