from rest_framework import serializers
from .models import ToDos
# Create your views here.


class ToDoSerializer(serializers.ModelSerializer):


    class Meta:
        model = ToDos
        fields = '__all__'
