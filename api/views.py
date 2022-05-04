from ast import Return
from cProfile import Profile
from django.shortcuts import render
from api.serializers import registrationSerializer,carmodelsSerializer,messageSerializers,profilesSerializer,carimagesSerializer,carsSerializers,companiesSerializer,repliesSerializers
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
import jwt,datetime
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
        data = Registration.objects.get(useremail = useremail)
        serialize = registrationSerializer(data)
        return Response(serialize.data)

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

@api_view(['POST'])
def user_login(request):
    details = request.data
    useremail = details['useremail']
    password = details['password']

    check_user = Registration.objects.filter(useremail = useremail)
    if check_user.exists():
        users = Registration.objects.get(useremail = useremail)
        if check_password(password , users.password):
            data = {
                'useremail':useremail,
                'password':password
            }
            payload = {
                'id': users.id,
                'exp': datetime.datetime.utcnow() + datetime.datetime(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret' ,algorithm='HS256').decode('utf-8')
            return Response({'jwt':token})
        return Response("wrong details provided, check and try again.")
    else:
        return Response("user dont exist.")

@api_view(['POST'])
def decode_user(request):
    details = request.data
    token = details['jwt']

    if not token:
        return Response("user unauthenticated")
    else:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        user =  Registration.objects.get(id = payload['id'])
        serialize = registrationSerializer(user)
        return Response(serialize.data)

@api_view(['POST'])
def add_profile(request):
    details = request.data
    user = details['user']
    image = details['image']
    contact = details['contact']

    getuser = Registration.objects.get(id = user)

    if getuser:
        checkprofile =  Profile.objects.get(contact = contact)
        if checkprofile:
            return Response({'warning':'profile already exist.'})
        else:
            new_profile = Profile(user = getuser,image = image, contact = contact)
            new_profile.save()
            return Response({'success':'profile added successfully.'})
    else:
        return Response({'error':'user unauthenticated.'})

@api_view(['GET'])
def get_profile(request, id):
    getuser = Registration.objects.get(id = id)

    if getuser:
        user_profile = Profile.objects.get(user = getuser)
        if not user_profile:
            return Response({'warning':'no profile matches this user.'})
        else:
            serialize = profilesSerializer(user_profile)
            return Response(serialize.data)
    else:
        return Return({'error':'user unauthenticated'})