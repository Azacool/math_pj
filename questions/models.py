from django.db import models
from django.contrib.auth.models import User


class Answers(models.Model):       
    variant1=models.CharField(max_length=50)
    variant2=models.CharField(max_length=50)
    variant3=models.CharField(max_length=50)

class Questions(models.Model):
    answer = models.ForeignKey(Answers, null=False, on_delete=models.CASCADE)
    image = models.ImageField(default='defualt.webp')
    text = models.TextField(null=False)
    def __str__(self) -> str:
        return self.answer

