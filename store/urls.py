from django.urls import path
from .views import (
    home, view_cart, search, checkout, track_order, cancel_order,
    admin_dashboard, customer_reviews, user_profile, customer_support
)

urlpatterns = [
    path('', home, name='home'),
    path('cart/', view_cart, name='view_cart'),
    path('search/', search, name='search'),
    path('checkout/', checkout, name='checkout'),
    path('track-order/<int:order_id>/', track_order, name='track_order'),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('customer-reviews/', customer_reviews, name='customer_reviews'),
    path('user-profile/<int:user_id>/', user_profile, name='user_profile'),
    path('customer-service/', customer_support, name='customer_service'),
]