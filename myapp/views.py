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
    return render(request, "menu.html")

def about(request):
    about_content = {'content': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, "about.html", about_content)

def book(request):
    return HttpResponse("Book Your Reservations Today")