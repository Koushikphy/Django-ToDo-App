from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from .serializers import ToDoSerializer
from rest_framework import serializers, viewsets
from .models import ToDos
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.forms import ModelForm

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