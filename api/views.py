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
    print(todo)
    serializer = ToDoSerializer(todo, many=True)
    print(serializer.data)
    return Response(serializer.data)
    if serializer.is_valid():
        # print(serializer.data)
        # return Response(serializer.data)
        return Response({
            "message":'gwgwg'
        })
    else:
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)