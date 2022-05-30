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