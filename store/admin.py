from django.contrib import admin
from .models import Category, Product, CartItem, Order, UserProfile, CustomerReview

# Customize Product display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)

# Customize CartItem display in admin
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name')

admin.site.register(CartItem, CartItemAdmin)

# Customize Order display in admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'status')

admin.site.register(Order, OrderAdmin)

# Customize CustomerReview display in admin
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')

admin.site.register(CustomerReview, CustomerReviewAdmin)

# Register other models without customization
admin.site.register(Category)
admin.site.register(UserProfile)
