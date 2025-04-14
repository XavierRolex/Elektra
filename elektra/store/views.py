from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist, Cart
#Homepage
def home(request):
    """
    It shows the homepage of the store.

    args:
        request (HttpRequest): The HTTP request object. It's a object that is used to request data from the server.

    Returns:
        HttpResponse: The rendered homepage template.
    """
    return render(request, 'store/home.html')

# View Wishlist
@login_required
def view_wishlist(request):
    """
    Display all wishlist items for the logged-in user.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Attributes:
        user (ForeignKey): The user who owns the wishlist.

    Returns:
        HttpResponse: Rendered wishlist page with the user's wishlist items.
        wishlist_items (QuerySet): All wishlist items for the logged-in user.
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist_items': wishlist_items})

# Add to Wishlist
@login_required
def add_to_wishlist(request, product_id):
    """
    Add products to the user's wishlist.

    Args:
        request (HttpRequest): The incoming HTTP request.
        product_id (int): The ID of the product to be added.

    Attributes:
        user (ForeignKey): The user who owns the wishlist.
        product (ForeignKey): The product to be added to the wishlist.
    
    Returns:
        HttpResponse: Redirect to the wishlist page.
    """
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('view_wishlist')

# Remove from Wishlist
@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove products from the user's wishlist.

    Args:
        request (HttpRequest): The incoming HTTP request.
        product_id (int): The ID of the product to be removed.

    Attributes:
        user (ForeignKey): The user who owns the wishlist.
        product (ForeignKey): The product to be removed from the wishlist.

    Returns:
        HttpResponse: Redirect to the wishlist page.
    """
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('view_wishlist')

# View Cart
@login_required
def view_cart(request):
    """
    Display all cart items for the logged-in user.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Attributes:
        user (ForeignKey): The user who owns the cart.
        cart_items (QuerySet): All cart items for the logged-in user.
        total (float): Total price of all items in the cart.
    
    Returns:
        HttpResponse: Rendered cart page with the user's cart items and total price.
    """
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

# Add to Cart
@login_required
def add_to_cart(request, product_id):
    """
    Add products to the user's cart.

    Args:
        request (HttpRequest): The incoming HTTP request.
        product_id (int): The ID of the product to be added.

    Attributes:
        user (ForeignKey): The user who owns the cart.
        product (ForeignKey): The product to be added to the cart.
        item (Cart): The cart item to be created or updated.
    
    Returns:
        HttpResponse: Redirect to the cart page.
    """
    product = get_object_or_404(Product, id=product_id)
    item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    return redirect('view_cart')

# Remove from Cart
@login_required
def remove_from_cart(request, product_id):
    """
    Remove products from the user's cart.

    Args:
        request (HttpRequest): The incoming HTTP request.
        product_id (int): The ID of the product to be removed.
    
    Attributes:
        user (ForeignKey): The user who owns the cart.
        product (ForeignKey): The product to be removed from the cart.
    
    Returns:
        HttpResponse: Redirect to the cart page.
    """
    Cart.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('view_cart')
