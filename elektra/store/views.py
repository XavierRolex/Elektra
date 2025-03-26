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

#Viewing Cart
@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'Cart Items': cart})

#Add to Cart
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Item, created = Cart.objects.get_or_create(user=request.user, product=product), defaults={'quantity': 1}
    if not created:
        Item.quantity += 1
        Item.save()
    return redirect('cart')

#Discard from Cart
@login_required
def disc_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Cart.objects.filter(user=request.user, product=product).delete()
    return redirect('cart')