from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from .models import Category, Location, Image


# Create your views here.
def welcome(request):
    images=Image.objects.all()
    locations= Location.objects.all()
    categories=Category.objects.all()
    return render(request,'index.html', {'images':images, 'locations':locations, 'categories':categories})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
    

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
    
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
