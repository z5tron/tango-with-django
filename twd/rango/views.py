from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    context_dict = { "boldmessage": "I am bold font from the context" }
    return render(request, "rango/index.html", context_dict)

def about(request):
    return HttpResponse("About <a href='{}'>Index</a>".format(reverse('index')))
