from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50, unique=True), 

    def save_category(self):
        self.save()


    def update_category(self, name):
        self.name = name
        self.save()

    
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=50, unique=True),

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id=id).update(name=name)

    @classmethod
    def display_all_location(cls):
        return cls.objects.all()

class Image(models.Model):
    #image field
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    location=models.ForeignKey('Location', on_delete=models.CASCADE)

    def save_image(self):
        self.save()
    
    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__name=location)
        return images    

    def update_image(self, name, description, location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    @classmethod
    def filter_by_category(cls, category):
        images = Image.objects.filter(category__name=category)
        return images

    
    
    def __str__(self):
        return self.name



    def delete_image(self):
        self.delete()