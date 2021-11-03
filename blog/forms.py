from django import forms
from .models import Post,ProfileView,NeibaV





class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('user_name', 'user_id','name','image','user_location')

    # widgets={
    #   'title': forms.TextInput(attrs={'class':'form-control'}),
    #   'author':forms.Select(attrs={'class':'form-control'}),
    #   # 'category':forms.Select(choices=choices_l,attrs={'class':'form-control'}),
    #   'body': forms.Textarea(attrs={'class':'form-control'})
    # } 
    
class ProfileUpdateForm(forms.ModelForm):
  

    class Meta:
        model = ProfileView
        fields = ['user_pic', 'user_email','house_location','user', 'user_email',  'user_bio', 'gender']

class MtaaForm(forms.ModelForm):
     

     class Meta:
         model=NeibaV
         fields = ['neiba','author','title','body']    