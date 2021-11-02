from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=300)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('home')




class Post(models.Model):
  
  title = models.CharField(max_length=200)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.CharField(max_length=200,default='supercar')
  images =  CloudinaryField( 'image', null=True, )
  body = models.TextField()

  def __str__(self):
    return self.title 

  def get_absolute_url(self):
    return reverse('home')