from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse(
        '''<center><h1>404:</h1>
        You got the wrong site, because that page is not found.<center>''')

def home(request):
    return HttpResponseNotFound('''Little Lemon!''')