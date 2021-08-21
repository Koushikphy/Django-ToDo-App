from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from .serializers import ToDoSerializer
from rest_framework import serializers, viewsets
from .models import ToDos
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view
from django.forms import ModelForm
from rest_framework.response import Response
from rest_framework import status



class ToDoViewSets(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ToDos.objects.all()
    serializer_class = ToDoSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)


class TodoForm(ModelForm):
    class Meta:
        model = ToDos
        fields = '__all__'


 

def index(request):
    return render(request, 'index.html',{
        "myVar" : "Simple ",
        'form':TodoForm()
    })



@api_view(['GET'])
def getListofTodo(request):
    todo = ToDos.objects.all()
    serializer = ToDoSerializer(todo, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleofTodo(request,todo_id):
    todo = ToDos.objects.get(pk=todo_id)
    serializer = ToDoSerializer(todo)
    return Response(serializer.data)



# NOTES:
# 1. pass data argument to the serializer class when only uning the dict instance, that, query set is like a list of dictionaries
#  so when passing the query set dont use the data argument

# as queryset is like a list like object so we have to provide many=true the serializer calll to serialize a list of jsons

# is_valid is only called when when you pass a dictionary json, posted from the user to validate it before save, so when a 
# get request the is_valid call does not make any sense.

# Since you are passing a QuerySet object, you must not provide the data argument.

# QuerySet is a list like object, so you should provide many=True while serialization.

# the is_valid() method only is applicable only if you pass a dictionary to the data argument, which is not here.