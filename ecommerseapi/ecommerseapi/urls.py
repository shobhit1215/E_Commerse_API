"""ecommerseapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import RegistrationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    #If we do POST request with username and password in the below url we will get the auth token 
    # path('api/auth/auth-token',obtain_auth_token,name='obtain-auth-token'),
    #After registration of a new user we call login url to get token and then do all the requests with that token
    path('auth/register',RegistrationAPIView.as_view(),name='register'),
    path('auth/login',obtain_auth_token,name='obtain-auth-token'),
    
]
