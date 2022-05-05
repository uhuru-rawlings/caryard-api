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
from api.views import register,resetpassword,user_login,decode_user,add_profile,get_profile,car_models,check_availability,post_cars,get_cars,reply_messages,getreplies
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
# from django.conf.urls import url
schema_view = get_schema_view(
   openapi.Info(
      title="CARYARD-KENYA API",
      default_version='v1',
      description="CAR-YARD KENYA",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="uhururawlings40@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/register/', register, name="registration"),
    path('api/reset/', resetpassword, name="reset_password"),
    path('api/login/', user_login, name="login"),
    path('api/getuser/', decode_user, name="getuser"),
    path('api/profiles/', add_profile, name="profiles"),
    path('api/profiles/userprofile/<int:id>/', get_profile, name="user_profile"),
    path('api/carmodels/', car_models, name="carmodels"),
    path('api/availability/', check_availability, name="availability"),
    path('api/post/cars/', post_cars, name="cars"),
    path('api/getall/cars/', get_cars, name="all_cars"),
    path('api/messages/replies/', reply_messages, name="reply_messages"),
    path('api/replies/', getreplies, name="replies"),
]
