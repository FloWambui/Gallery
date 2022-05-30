from django.http  import HttpResponse
from django.shortcuts import render
from .models import Category, Location


# Create your views here.
def welcome(request):
    locations = Location.get_locations()
    categories = Category.objects.all()
    return render(request,'index.html')

