from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.

class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='Spain')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_location()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update_location(self):
        new_location = 'Kenya'
        self.location.update_location(self.location.id,new_location)
        changed_location = Location.objects.filter(name='Kenya')
        self.assertTrue(len(changed_location) > 0)

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(name='Rose Period')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class ImageTestCase(TestCase):

    def setUp(self):
        Image.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
        
        )

    def test_image_name(self):
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.name, "Test Image")

    def test_image_description(self):
            image = Image.objects.get(name="Test Image")
            self.assertEqual(image.description, "Test Description")
        

