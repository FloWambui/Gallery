from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

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
    def get_location(cls):
        return cls.objects.all()



class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id=id).update(name=name)


class Image(models.Model):
    #image field
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    location=models.ForeignKey('Location', on_delete=models.CASCADE)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)

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