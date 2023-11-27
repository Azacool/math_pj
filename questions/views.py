from django.shortcuts import render
from django.http import HttpResponse
from .models import Answers,Questions
def questions(request):
    questions = Questions.objects.all()
    for question in questions:
        print(question.image)
    return render(request, 'home.html', {'questions':questions})

