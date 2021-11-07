from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime as dt
from .models import Neighbourhood,Business,Post,User
from .forms import UserCreationForm,UserChangeForm, UpdateProfileForm,UpdateUserForm,BusinessForm,PostForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views import generic
from django.contrib.auth import logout as django_logout
from django.urls import reverse_lazy

# Create your views here.
class UserRegister(generic.CreateView):
  form_class= UserCreationForm
  template_name='registration/register.html'
  success_url= reverse_lazy('login')


class UserEdit(generic.UpdateView):
  form_class= UserChangeForm
  template_name='registration/edit_profile.html'
  success_url= reverse_lazy('home')

  def get_object(self):
    return self.request.user

def home(request):
    post=Post.objects.all()
    
    date = dt.date.today()
    # business = Business.get_allbusiness()
    all_neighbourhoods = Neighbourhood.get_neighbourhoods()
    
    
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        neighbourhoods = request.GET.get("neighbourhood")
        searched_neighbourhood = Business.get_by_neighbourhood(neighbourhoods)
        all_posts = Post.get_by_neighbourhood(neighbourhoods)
        infos = f"{neighbourhoods}"
        all_neighbourhoods = Neighbourhood.get_neighbourhoods()        
        
        return render(request, 'home.html', {"infos":infos,"location": searched_neighbourhood,
                                               "all_neighbourhoods":all_neighbourhoods, "all_posts":all_posts,'post':post})

    else:
        infos = "No Neighbourhood Found!"

    return render(request, 'home.html', {"date": date, "all_neighbourhoods":all_neighbourhoods,'post':post})

login_required(login_url='/accounts/login/')
def profile(request, username):
    return render(request, 'profile.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'editprofile.html', {'user_form': user_form, 'prof_form': prof_form})
    
login_required(login_url='/accounts/login/')
def search_businesses(request):
    if 'keyword' in request.GET and request.GET['keyword']:
        search_term = request.GET.get('keyword')
        searched_blogs = Business.search_business(search_term)
        infos = f"(search_term)"
        
        return render(request, 'search.html', {"infos": infos, "businesses": searched_blogs})
    else:
        infos = "No business searched"
        return render(request, 'search.html', {"infos": infos})
    

def get_business(request, id):

        blog = Business.objects.get(pk=id)
    # try:
        
    # except ObjectDoesNotExist:
    #     raise Http404()
    
    
        return render(request, "blogs.html", {"blog": blog})
    
login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    profile = request.user.profile
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.Admin = current_user
            blog.admin_profile = profile
            blog.save()
        return redirect('home')

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')

    
login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = request.user.profile
    neighbourhood = request.user.profile.neighbourhood

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.author_profile = profile
            post.neighbourhood = neighbourhood
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'add_post.html', {"form": form})

