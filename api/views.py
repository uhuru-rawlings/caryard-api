from ast import Return
from cProfile import Profile
from multiprocessing import AuthenticationError
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
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            # token = jwt.encode(payload, 'secret' ,algorithm='HS256')
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
        try:
           payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            # raise AuthenticationError("user unauthenticated")
            return Response("user unauthenticated")
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
        checkprofile =  Profiles.objects.get(contact = contact)
        if checkprofile:
            return Response({'warning':'profile already exist.'})
        else:
            new_profile = Profiles(user = getuser,image = image, contact = contact)
            new_profile.save()
            return Response({'success':'profile added successfully.'})
    else:
        return Response({'error':'user unauthenticated.'})

@api_view(['GET'])
def get_profile(request, id):
    getuser = Registration.objects.get(id = id)

    if getuser:
        user_profile = Profiles.objects.get(user = getuser)
        if not user_profile:
            return Response({'warning':'no profile matches this user.'})
        else:
            serialize = profilesSerializer(user_profile)
            return Response(serialize.data)
    else:
        return Return({'error':'user unauthenticated'})

@api_view(['GET'])
def car_models(request):
    cars = CarModels.objects.all()
    modelsc = ["Abarth","Acura","Alfa Romeo","BMW","Aston Martin","Audi","Bently","Buick",
                "Cadillac","Chevrolet","Chrysler","Citroen","Dacia","Doege","Ferrari","Fiat",
                "Ford","GMC","Honda","Hummer","Hyundai","Infiniti","Isuzu","Jagua","Jeep",
                "Kia","Lamboghini","Lancia","Land Rover","Lexus","Lincoln","Lotus","Maserati",
                "Mazda","Mercedes-Benz","Mercury","Mini","Mistubishi","Nisan","Opel","Peugeot",
                "Pontiac","Porsche","Ram","Renault","Saab","Saturn","Scion","Seat","Skoda","Smart",
                "SsangYong","Subaru","Suzuki","Tesla","Toyota","Volkswagen","Volvo","Wiesmann"]
    companies = Companies.objects.all()
    if companies:
        pass
    else:
        for y in modelsc:
            new_company = Companies(companyname = y)
            new_company.save()
    companies = Companies.objects.all()
    if cars:
        serialize = carmodelsSerializer(cars, many= True)
        return Response(serialize.data)
    else:
        for x in modelsc:
            for v in companies:
               if v.companyname == x:
                    new_models = CarModels(modelname = x,company = v)
                    new_models.save()
        cars = CarModels.objects.all()
        serialize = carmodelsSerializer(cars, many= True)
        return Response(serialize.data)

@api_view(['POST'])
def check_availability(request):
    details = request.data
    user = details['id']
    cars = details['carid']
    message = details['messages']

    user = Registration.objects.get(id = id)
    cars = Cars.objects.get(id = id)
    if not user:
        return Response({'error':'user unauthenticated'})
    else:
        new_message = Messages(user = user, cars = cars, message = message)
        new_message.save()

@api_view(['POST'])
def post_cars(request):
    details = request.data
    user = details['id']
    carmodel = details['carmodel']
    years_of_service = details['years_of_service']
    Fuelconsumption = details['Fuelconsumption']
    description = details['description']
    cardetails = details['cardetails']
    interior = details['interior']
    exterior = details['exterior']
    
    user = Registration.objects.get(id = user)
    if user:
        new_car = Cars(user = user, carmodel = carmodel, years_of_service = years_of_service, Fuelconsumption = Fuelconsumption, description =description)
        new_car.save()

        cardetails = Cars.objects.filter(user = user)
        last = len(cardetails)
        carimages = CarImages(cardetails = cardetails[last - 1],interior = interior, exterior = exterior)
        carimages.save()
        return Response({'success':'posted succefully.'})
    else:
        return Response({'error':'user unauthenticated'})

@api_view(['GET'])
def get_cars(request):
    cars = Cars.objects.all()

    if not cars:
        return Response([])
    else:
        serialize = carsSerializers(cars, many = True)
        return Response(serialize.data)

@api_view(['GET'])
def get_images(request):
    cars = CarImages.objects.all()

    if not cars:
        return Response([])
    else:
        serialize = carimagesSerializer(cars, many = True)
        return Response(serialize.data)


@api_view(['POST'])
def reply_messages(request):
    details = request.data
    user = details['userid']
    messageid = details['messageid']
    message = details['userid']

    user = Registration.objects.all()
    messageid = Messages.objects.get(id = messageid)
    if not user:
        return Response({'error':'user unauthenticated.'})
    else:
        new_reply = Replies(user = user, messageid = messageid ,message = message)
        new_reply.save()
        return Response({'success':'message reply sent successfully.'})

@api_view(['GET'])
def getreplies(request):
    replies = Replies.objects.all()

    if not replies:
        return Response([])
    else:
        serialize = repliesSerializers(replies, many = True)
        return Response(serialize.data)