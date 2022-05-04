from django.shortcuts import render
from serializers import registrationSerializer,carmodelsSerializer,messageSerializers,profilesSerializer,carimagesSerializer,carsSerializers,companiesSerializer,repliesSerializers
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin
from rest_framework.views import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

@api_view(['GET'])
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