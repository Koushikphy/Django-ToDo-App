from django.db import models

# Create your models here.

class ToDos(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    completed = models.BooleanField()
    priority = models.IntegerField(blank=True)
    # also have to add datefield

    def __str__(self) -> str:
        return self.title