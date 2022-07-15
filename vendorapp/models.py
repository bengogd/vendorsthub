from itertools import product
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    product_description = models.TextField(blank=True)
    tags = TaggableManager()
    sales_location = models.CharField(max_length=300)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    updated = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

class Shopper(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.product.title


  

class Product_Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.product.title