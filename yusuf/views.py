from unicodedata import name
from django.shortcuts import render

# Create your views here.


#from django.http import HttpResponse
 
 
#def index(request):
#  return HttpResponse("Hello Geeks")


# Create your views here.
def home_view(request):
 
    # logic of view will be implemented here
    print(request.POST)
    
    return render(request, "home.html")

