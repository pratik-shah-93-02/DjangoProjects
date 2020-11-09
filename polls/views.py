#from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("Hello Team MVD, Now we can design web based user interface for any aplication.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

