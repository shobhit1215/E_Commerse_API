from rest_framework import serializers

from .models import Category,Book,Product,Cart
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=50,min_length=6)
    username = serializers.CharField(max_length=50,min_length=6)
    password=serializers.CharField(max_length=150,write_only=True)

    
    class Meta:
        model = User
        fields=('first_name','last_name','email','username','password')
    def validate(self,args):
        email = args.get('email',None)
        username = args.get('username',None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'email':('username already exists')})
        return super().validate(args)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



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