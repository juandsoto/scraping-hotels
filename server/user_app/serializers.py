from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['user_id','first_name', 'last_name', 'password', 'role', 'state', 'email']