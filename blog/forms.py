from django import forms
from .models import Post,Category





class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'author','category','images','body')

    widgets={
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.Select(attrs={'class':'form-control'}),
      # 'category':forms.Select(choices=choices_l,attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'})
    } 
    