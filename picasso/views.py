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
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Category.search_by_category(search_term)
        message = f"{search_term}"
    

        return render(request, 'search.html', {"message": message, "categories": searched_images})

    else:
    
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
