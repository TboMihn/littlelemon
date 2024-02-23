from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to LittleLemon</h1>")

def menu(request):
    return HttpResponse("Menu")

def about(request):
    return HttpResponse("About Us")

def book(request):
    return HttpResponse("Book Your Reservations Today")