from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import ToDos
# Create your views here.
from django.contrib.auth import authenticate, login

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDos
        # fields = '__all__'
        exclude = ['user']
    
    # def update(self, instance, validated_data):
    #     print(validated_data,'------------------------')
    #     return super().update(instance, validated_data)

    def save(self, **kwargs):
        # print('inside serializer', kwargs, self.context['request'].user)
        kwargs['user'] = self.context['request'].user
        # print('777777777777777777777777777777777')
        return super().save(**kwargs)



# user serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = ('username', 'email', 'id')
        # fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = ('username', 'email', 'id', 'password')
        extra_kwargs={'password':{
            'write_only' : True
        }}
        # fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user #super().create(validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
     

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
        
            return user
        raise ValidationError("incorrect password")
        # return super().validate(attrs)