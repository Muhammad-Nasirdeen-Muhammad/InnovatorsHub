from django.http import HttpResponse
from django.shortcuts import render
# from .models import UserSubmission

def Home(request):
    return HttpResponse("Home page")
def feed(request):
    return HttpResponse("Feed")