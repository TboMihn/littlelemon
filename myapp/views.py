from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import LogForm

# Create your views here.

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)


# Main Views
def home(request):
    return HttpResponse("<h1>Welcome to LittleLemon</h1>")

def menu(request):
    return HttpResponse("Menu")

def about(request):
    about_content = {"about": "Based in Seattle, WA, Little Lemon is a trendy restaurant for all ages."}
    return render(request, "about.html", about_content)

def book(request):
    return HttpResponse("Book Your Reservations Today")