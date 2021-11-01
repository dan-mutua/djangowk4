from django.db import models

# Create your models here.
class BlogView(model.Model):
  category = models.ForeignKey(Mycategory,null=True,on_delete=models.CASCADE)
  body=models.TextField(blank=True)
  name = models.CharField(max_length=100)
  image=CloudinaryField()
  user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
  location=models.ForeignKey(Location,null=True,on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood,null=True,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)


   # create post
    def create_post(self):
        self.save()

    # delete post
    def delete_post(self):
        self.delete()

    # update post
    def update_post(self):
        self.update()

    # search post
    @classmethod
    def search_by_title(cls, search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post

    # find post by id
    @classmethod
    def find_post(cls, id):
        post = cls.objects.get(id=id)
        return post

    def __str__(self):
        return self.title