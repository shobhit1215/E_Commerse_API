from rest_framework import serializers

from .models import Category,Book,Product,Cart

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields =('id','title')
        model = Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','author','category','isbn','pages','price','stock','description','imageURL','status','date_created')
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','product_tag','name','category','price','stock','imageURL','status','date_created')
        model = Product

class CartSerializer(serializers.ModelSerializer):
    # books=BookSerializer(read_only=True, many=True)
    # products=ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ('cart_id','created_at','books','products')