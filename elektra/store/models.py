from django.db import models
from django.contrib.auth.models import User  # Importing the built-in User model

# Product containing all product info
class Product(models.Model):

    """
    It Represents a product in the store.

    Attributes:
        name (str): The name of the product.
        price (Decimal): The price of the product.
        description (str): A detailed description of the product.
        image (ImageField): An image of the product.
        created_at (DateTime): The date and time when the product was created.
    """
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    """
    It Represents a user's wishlist.

    Attributes:
        user (ForeignKey): The user who owns the wishlist.
        product (ForeignKey): The product in the wishlist.
        created_at (DateTime): The date and time when the wishlist item was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.product.name}"

class Cart(models.Model):
    """
    It Represents a user's shopping cart.
    
    Attributes:
        user (ForeignKey): The user who owns the cart.
        product (ForeignKey): The product in the cart.
        quantity (int): The quantity of the product in the cart.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.quantity} x {self.product.name}"
