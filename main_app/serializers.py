from django.contrib.auth.models import Group, User
from .models import Cat
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
