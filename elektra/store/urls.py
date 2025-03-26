from django.urls import path
from . import views

urlpatterns = [
    #path to sriti's home page.
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/del_from_wishlist/<int:product_id>/', views.del_from_wishlist, name='del_from_wishlist'),
    path('cart/', views.cart, name='cart'),
    path('cart/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/disc_from_cart/<int:product_id>/', views.disc_from_cart, name='disc_from_cart'),
]