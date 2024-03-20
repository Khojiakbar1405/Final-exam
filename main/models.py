from django.db import models
from django.contrib.auth.models import User
from functools import reduce


# Category uchun class
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



# Product uchun class
class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount_price = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        null=True,
        blank=True 
    )
    image = models.ImageField(upload_to='image/')


    @property 
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0
        

    @property 
    def is_active(self):
        return self.quantity > 0 
    


# Cart uchun class
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    @property
    def quantity(self):
        quantity = 0
        products = CartProduct.objects.filter(product_id = self.id)
        for i in products:
            quantity +=i.quantity
        return quantity

    @property
    def total_price(self):
        result = 0
        for i in CartProduct.objects.filter(cart_id=self.id):
            result +=(i.product.price)*i.quantity
        return result



# CartProduct uchun class
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    @property
    def total_price(self):
        if self.product.is_discount:
            result = self.product.discount_price * self.quantity
        else:
            result = self.product.price * self.quantity
        return result



# Order uchun class 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=[
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ], default='PENDING')

    def __str__(self):
        return f"Order: {self.id} - {self.user.username} - {self.status}"


    @property
    def total_price(self):
        result = 0
        for i in CartProduct.objects.filter(cart_id=self.id):
            result +=(i.product.price)*i.quantity
        return result