from statistics import mode
from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserEditSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'age', 'preofession', 'country', 'state', 'city', 
        'university', 'college', 'working_instituition', 'bio']



# class MatchSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = MatchList
#         fields = ['user', 'match']