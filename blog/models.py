from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save




# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=300)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('home')

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Prefer not to say')
   )

class Location(models.Model):
    location=models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.location
class Post(models.Model):
  
  # title = models.CharField(max_length=200)
  # author = models.ForeignKey(User, on_delete=models.CASCADE)
  # category = models.CharField(max_length=200,default='supercar')
  # images =  CloudinaryField( 'image', null=True, )
  # body = models.TextField()
  user_name = models.OneToOneField(User,on_delete=models.CASCADE)
  user_id = models.PositiveIntegerField(default=0)
  name = models.CharField(max_length=200)
  user_location=models.ForeignKey(Location,on_delete=models.CASCADE)
  image = CloudinaryField("image")
  date = models.DateTimeField(auto_now_add=True)

  @classmethod
  def get_mtaa(cls):
        neiba = Post.objects.all()
        return neiba

  class Meta:
        ordering = ['name']

  @classmethod
  def search_mtaa(cls,searchmtaa):
        neiba= cls.objects.filter(id__icontains = searchmtaa)
        return neiba

  def __str__(self):
    return self.title 

  def get_absolute_url(self):
    return reverse('home')

class NeibaV(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 
    title = models.CharField(max_length = 300)
    neiba = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

    def __str__(self):
	    return self.title
    def save_posts(self):
	    self.save()

    def delete_posts(self):
	    self.delete() 
class ProfileView(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_email = models.CharField(null=True, max_length=255)
    phone_number = models.IntegerField(null=True)
    user_bio = models.CharField(blank=True,max_length=255)
    house_location = models.CharField(blank=True,max_length=255)
    user_pic = CloudinaryField('image')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=11,  default='Male')

    def __str__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfileView.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)


    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    post_save.connect(save_user_profile, sender=User)


    class Meta:
        ordering = ('-user',)


    @classmethod
    def getProfileByName(cls, username):
        uprofile = cls.objects.filter(username=username)
        return uprofile

