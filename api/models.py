from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ToDos(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    completed = models.BooleanField()
    priority = models.IntegerField( default=1,
        choices=[(i,i) for i in range(1,4)])
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    duedate= models.DateTimeField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title