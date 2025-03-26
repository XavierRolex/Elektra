from django.shortcuts import render, redirect
from .models import Product, Wishlist, Cart
from django.contrib.auth.decorators import login_required

#Viewing Wishlist
@login_required
def wishlist (request):
    wishlist = Wishlist.objects.filter(user=request.user) #retrieving wishlist of the user
    return render(request, 'store/wishlist.html', {'wishlist': wishlist})

#Add to Wishlist
@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

#Remove from Wishlist
@login_required
def del_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')