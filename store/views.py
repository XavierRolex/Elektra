from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import CartItem, Product, Order, CustomerReview, UserProfile
from django.contrib.auth.decorators import login_required

# View for the home page
def home(request):
    """Display all products on the home page."""
    products = Product.objects.all()  # Fetch all products
    return render(request, 'store/home.html', {'products': products})

# View for displaying cart items
@login_required
def view_cart(request):
    """Display all items in the user's cart."""
    cart_items = CartItem.objects.filter(user=request.user)  # Fetch cart items for the logged-in user
    return render(request, 'store/cart.html', {'cart_items': cart_items})

# View for searching products
def search(request):
    """Search for products by name."""
    query = request.GET.get('q', '')  # Get the search query from the request
    products = Product.objects.filter(name__icontains=query)  # Filter products by name
    return render(request, 'store/search_results.html', {'products': products, 'query': query})

# View for checkout
@login_required
def checkout(request):
    """Display the checkout page with cart items and total price."""
    cart_items = CartItem.objects.filter(user=request.user)  # Fetch cart items for the logged-in user
    total_price = sum(item.product.price * item.quantity for item in cart_items)  # Calculate total price
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# View for placing an order
@login_required
def place_order(request):
    """Place an order for the items in the user's cart."""
    cart_items = CartItem.objects.filter(user=request.user)  # Fetch cart items for the logged-in user
    if not cart_items.exists():
        return JsonResponse({'error': 'Your cart is empty'}, status=400)

    total_price = sum(item.product.price * item.quantity for item in cart_items)  # Calculate total price
    order = Order.objects.create(user=request.user, total_price=total_price)  # Create a new order

    # Associate cart items with the order
    for item in cart_items:
        order.items.create(product=item.product, quantity=item.quantity)

    # Clear the cart
    cart_items.delete()
    return JsonResponse({'message': 'Order placed successfully'})

# View for tracking an order
@login_required
def track_order(request, order_id):
    """Track the status of a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)  # Fetch the order for the logged-in user
    return render(request, 'store/track_order.html', {'order': order})

# View for canceling an order
@login_required
def cancel_order(request, order_id):
    """Cancel a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)  # Fetch the order for the logged-in user
    if order.status == 'Cancelled':
        return JsonResponse({'error': 'Order is already cancelled'}, status=400)

    order.status = 'Cancelled'  # Update the order status to "Cancelled"
    order.save()
    return JsonResponse({'message': 'Order canceled successfully'})

# View for the admin dashboard
@login_required
def admin_dashboard(request):
    """Display all orders in the admin dashboard."""
    orders = Order.objects.all()  # Fetch all orders
    return render(request, 'store/admin_dashboard.html', {'orders': orders})

# View for customer reviews
def customer_reviews(request):
    """Display all customer reviews."""
    reviews = CustomerReview.objects.all()  # Fetch all customer reviews
    return render(request, 'store/customer_reviews.html', {'reviews': reviews})

# View for user profile
@login_required
def user_profile(request, user_id):
    """Display the profile of a specific user."""
    profile = get_object_or_404(UserProfile, user__id=user_id)  # Fetch the user profile
    return render(request, 'store/user_profile.html', {'profile': profile})

# View for customer support
def customer_support(request):
    """Display the customer support page."""
    return render(request, 'store/customer_support.html')