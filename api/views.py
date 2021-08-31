from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.regex_helper import contains
from .serializers import LoginSerializer, RegistrationSerializer, ToDoSerializer, UserSerializer
from rest_framework import fields, serializers, viewsets
from .models import ToDos
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view
from django.forms import ModelForm
from rest_framework.response import Response
from rest_framework import status
import os 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from knox.models import AuthToken
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





class ToDoViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToDos.objects.all()
    serializer_class = ToDoSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    authentication_classes = [SessionAuthentication, BasicAuthentication]


    def get_queryset(self):
        return ToDos.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        print(request.data)

        ser = self.serializer_class(data=request.data)
        ser.is_valid()
        print(ser.errors)  # force to show errors
        return super().create(request, *args, **kwargs)




class TodoForm(ModelForm):
    class Meta:
        model = ToDos
        fields = '__all__'




@api_view(["POST"])
def logOutUser(request):
    logout(request)
    return Response({
        "logout": "success"
    })


class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # _, token = AuthToken.objects.create(user)
        # login(request, user)  # if you readily want to login the user after register
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            # "token":token
        })




class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            messages.warning(request,"Invalid username, password")
            return Response({
                "error": "invalid username password"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = serializer.validated_data
            print(user,'==================')
            login(request, user)
            # messages.success(request, "Log in success")
            # _, token = AuthToken.objects.create(user)
            return Response({
                "user" : UserSerializer(user, context=self.get_serializer_context()).data,
                # "token":token
            })





def index(request):
    # return render(request, 'base.html')
    # return render(request, 'index.html')

    # print(request.user, request.user.is_authenticated)
    if(request.user.is_authenticated) :
        return render(request, 'index.html')
    else:
        return render(request, 'user.html')



# class UserViewSets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer






# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')



# def userView(request):
#     return render(request,'user.html',{
#         "form" : UserForm
#     })




# @api_view(['GET'])
# def getListofTodo(request):
#     todo = ToDos.objects.all()
#     serializer = ToDoSerializer(todo, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getSingleofTodo(request,todo_id):
#     todo = ToDos.objects.get(pk=todo_id)
#     serializer = ToDoSerializer(todo)
#     return Response(serializer.data)


# @api_view(['POST',"GET"])
# def putTodo(request):
#     if request.method =='POST':
#         serializer = ToDoSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#     else:
#         todo = ToDos.objects.all()
#         serializer = ToDoSerializer(todo, many=True)
#         return Response(serializer.data)






# NOTES:
# 1. pass data argument to the serializer class when only uning the dict instance, that, query set is like a list of dictionaries
#  so when passing the query set dont use the data argument

# as queryset is like a list like object so we have to provide many=true the serializer calll to serialize a list of jsons

# is_valid is only called when when you pass a dictionary json, posted from the user to validate it before save, so when a 
# get request the is_valid call does not make any sense.

# Since you are passing a QuerySet object, you must not provide the data argument.

# QuerySet is a list like object, so you should provide many=True while serialization.

# the is_valid() method only is applicable only if you pass a dictionary to the data argument, which is not here.