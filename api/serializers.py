from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import ToDos
# Create your views here.


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDos
        # fields = '__all__'
        exclude = ['user']
    
    def save(self, **kwargs):
        # print('inside serializer', kwargs, self.context['request'].user)
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        # fields = ('username', 'email', 'id')
        fields = '__all__'
