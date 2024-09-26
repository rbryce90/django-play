# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
# from django.template.loader import render_to_string
from django.template.loader import render_to_string

def home(request):
    return render(request, "base.html", {"title": "Bryce Site"}) 

def about(request):
    # return HttpResponse("This is the About Page!")
    return render(request, "myapp/home.html") 