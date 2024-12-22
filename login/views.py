from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse


def login(request):
    return render(request, "login.html")

def submit_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"status: success, Name: {name}")
    return HttpResponse(f"Status failure")