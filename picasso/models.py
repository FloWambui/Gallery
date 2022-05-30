from django.db import models

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