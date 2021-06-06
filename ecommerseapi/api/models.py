from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    author = models.CharField(max_length=100,default='John Doe')
    isbn = models.CharField(max_length=20)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageURL = models.URLField(max_length=500)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering=['-date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)

class Cart(models.Model):
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ForeignKey(Book,on_delete=models.CASCADE,default=1)
    products = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)

    class Meta:
        ordering = ['cart_id','-created_at']

    def __str__(self):
        return f'{self.cart_id}'
