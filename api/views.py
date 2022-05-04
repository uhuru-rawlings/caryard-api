from django.shortcuts import render
from api.serializers import registrationSerializer,carmodelsSerializer,messageSerializers,profilesSerializer,carimagesSerializer,carsSerializers,companiesSerializer,repliesSerializers
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def register(request):
    details = request.data
    username = details['username']
    useremail = details['useremail']
    password = details['password']

    check_user = Registration.objects.filter(useremail = useremail)
    if check_user.exists():
        return Response('user with this email already exist')
    else:
        new_user = Registration(useremail = useremail, username = username, password = make_password(password))
        new_user.save()
        data = {
            'useremail':useremail,
            'username':username,
        }
        serialize = registrationSerializer(data, many=True)
        return Response(serialize)

@api_view(['POST'])
def resetpassword(request):
    details = request.data
    useremail = details['useremail']
    password = details['password']

    check_user = Registration.objects.filter(useremail = useremail)
    if check_user.exists():
        users = Registration.objects.get(useremail = useremail)
        users.password = make_password(password)
        users.save()
        return Response("password reset succesfull")
    else:
        return Response("user dont exist.")