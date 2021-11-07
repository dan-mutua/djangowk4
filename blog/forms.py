from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from crispy_forms.helper import FormHelper
 
 
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')
        

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'picture', 'neighbourhood']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
          'address': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['Admin', 'pub_date', 'admin_profile']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['Author', 'pub_date', 'author_profile', 'neighbourhood']
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }

class SignupForm(UserCreationForm):
  name= forms.CharField(max_length=200)
  neighborhood= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
 

  class Meta:
    model = User
    fields= ('username', 'last_name','email', 'password1','password2')

    def __init__(self,*args,**kwargs):
      super(SignupForm, self).__init__(*args,**kwargs)

      self.fields['username'].widget.attrs['class':'form-control']
      self.fields['password1'].widget.attrs['class':'form-control']
      self.fields['password2'].widget.attrs['class':'form-control']


class EditProfile(UserChangeForm):
  email = forms.EmailField(widget=forms.EmailInput)
  first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
 

  class Meta:
    model = User
    fields= ('username', 'last_name','email', 'password')          