"""caryard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from api.views import register,resetpassword,user_login,decode_user,add_profile,get_profile,car_models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register, name="registration"),
    path('api/reset/', resetpassword, name="reset_password"),
    path('api/login/', user_login, name="login"),
    path('api/getuser/', decode_user, name="getuser"),
    path('api/profiles/', add_profile, name="profiles"),
    path('api/profiles/userprofile/<int:id>/', get_profile, name="user_profile"),
    path('api/carmodels/', car_models, name="carmodels"),
]
