from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Picasso Gallery.Capture every moment')