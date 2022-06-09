from django.test import TestCase
from .models import Post,Profile

# Create your tests here.
class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.self= Post(author="matrin",description="Holla",image="madia")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.self))
    
    # Testing Save Method
    def test_save_method(self):
        self.self.save_post()
        images= Post.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Post.objects.all().delete()
    
    
  