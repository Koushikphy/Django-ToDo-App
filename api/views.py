from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from .serializers import ToDoSerializer
from rest_framework import serializers, viewsets
from .models import ToDos


class ToDoViewSets(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ToDos.objects.all()
    serializer_class = ToDoSerializer



def index(request):
    return render(request, 'index.html',{
        "myVar" : "Simple "
    })