from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to PSUSphere</h1><p>The student organization management system is running.</p>")
