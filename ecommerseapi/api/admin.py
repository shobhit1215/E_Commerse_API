from django.contrib import admin
from .models import Category,Book,Product,Cart
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','category','isbn','price','pages','stock','description','imageURL','status','date_created']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_tag','name','category','price','stock','imageURL','status','date_created']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id','created_at','books','products']

