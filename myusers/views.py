from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegister(generic.CreateView):
  form_class= UserCreationForm
  template_name='registration/register.html'
  success_url= reverse_lazy('login')

class LoginView(AuthenticationForm):
  form_class=

class UserEdit(generic.UpdateView):
  form_class= UserChangeForm
  template_name='registration/edit_profile.html'
  success_url= reverse_lazy('home')

  def get_object(self):
    return self.request.user


