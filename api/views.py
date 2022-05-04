from django.shortcuts import render
from serializers import registrationSerializer
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin
from rest_framework.views import api_view
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
