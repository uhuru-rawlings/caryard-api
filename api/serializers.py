from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin

#serializers

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id','useremail','username']

class profilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['user','image','contact','date_added']
class carmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = ['modelname','company','date_added']
class messageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['user','cars','message','date_sent']
class carimagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ['cardetails','interior','exterior','date_added']
class carsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['user','carmodel','years_of_service','Fuelconsumption','description','date_added']

class companiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['companyname','date_added']
class repliesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ['user','message','date_sent']
    