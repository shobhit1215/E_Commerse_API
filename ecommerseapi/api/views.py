from django.shortcuts import render
from rest_framework import generics
from .models import Category,Book,Product,Cart
from .serializers import RegistrationSerializer,CategorySerializer,BookSerializer,ProductSerializer,CartSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
import uuid
from rest_framework import serializers
# Create your views here.

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId":str(uuid.uuid4()),
                "Message":"User Created",
                "User":serializer.data},status=status.HTTP_201_CREATED
                )
        return Response({"Errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =(permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListBook(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
