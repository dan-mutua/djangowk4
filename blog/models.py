from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class BlogView(models.Model):
  category = models.ForeignKey(Mycategory,null=True,on_delete=models.CASCADE)
  body=models.TextField(blank=True)
  name = models.CharField(max_length=100)
  image=CloudinaryField()
  user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
  location=models.ForeignKey(Location,null=True,on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood,null=True,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)


   
  def create_post(self):
        self.save()

    
  def delete_post(self):
        self.delete()

    
  def update_post(self):
        self.update()

    
  @classmethod
  def search_by_title(cls, search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post

   
  @classmethod
  def find_post(cls, id):
        post = cls.objects.get(id=id)
        return post

  def __str__(self):
        return self.name

class Mycategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name        

 
class Theprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


# business class model
class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # create business
    def create_business(self):
        self.save()

    # delete business
    def delete_business(self):
        self.delete()

    # update business
    def update_business(self):
        self.update()

    # search business
    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    # find business by id
    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def __str__(self):
        return self.name


# contact class model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        NeighbourHood, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # create contact
    def create_contact(self):
        self.save()

    # delete contact
    def delete_contact(self):
        self.delete()

    # update contact
    def update_contact(self):
        self.update()

    # search contact
    @classmethod
    def search_by_name(cls, search_term):
        contact = cls.objects.filter(name__icontains=search_term)
        return contact

    # find contact by id
    @classmethod
    def find_contact(cls, id):
        contact = cls.objects.get(id=id)
        return contact

    def __str__(self):
        return self.name        