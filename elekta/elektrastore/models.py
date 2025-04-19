from django.db import models
import datetime

#Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Customer

#Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.name

#Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
