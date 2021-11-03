from django.shortcuts import render
from .models import Post,NeibaV, ProfileView
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class HomePage(ListView):
  model= NeibaV
  template_name= 'home.html'

class  NeibaD(DetailView):
  model = ProfileView
  template_name='neiba_detail.html'

class Addp(CreateView):
  model = Post
  form_class=PostForm
  template_name= 'addphoto.html'  

class UpdateProfile( UpdateView):
    model = ProfileView
    fields = ['user_pic', 'house_location','user', 'user_email', 'phonenumber', 'user_bio', 'gender']
    template_name = 'profileedit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        raise( 'Your Account Settings were updated successfully!')
        return reverse('profile')



class DeleteViewB(DeleteView):
  model = Post
  template_name= 'delete.html'
  success_url= reverse_lazy('home')
