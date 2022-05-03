from pyexpat import model
from rest_framework import serializers
from api.models import Registration,Profiles,CarModels,Messages,CarImages,Cars,Companies,Replies,Lastlogin

#serializers

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['useremail','username','password']
