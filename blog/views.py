from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class HomePage(ListView):
  model= Post
  template_name= 'home.html'

class  BlogD(DetailView):
  model = Post
  template_name='p_detail.html'

class Addp(CreateView):
  model = Post
  form_class=PostForm
  template_name= 'addphoto.html'  

class AddCategory(CreateView):
  model = Post
  fields= '__all__'
  template_name= 'addcategory.html'    


class UpdateViewB(UpdateView):
  model = Post
  template_name= 'update.html'
  fields = ('title', 'author','body')

class DeleteViewB(DeleteView):
  model = Post
  template_name= 'delete.html'
  success_url= reverse_lazy('home')
