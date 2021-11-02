from django.shortcuts import render
from os import name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Business,NeighbourHood,Location,BlogView,Contact,Mycategory,Theprofile
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def blog(request):
    current_user = request.user
    # get current user neighbourhood
    profile = Theprofile.objects.filter(user_id=current_user.id).first()
    # check if user has neighbourhood
    if profile is None:
        profile = Theprofile.objects.filter(
            user_id=current_user.id).first()  # get profile
        blog = BlogView.objects.filter(user_id=current_user.id)
        # get all locations
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        category = Mycategory.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        # redirect to profile with error message
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": blog})
    else:
        neighbourhood = profile.neighbourhood
        # get all posts in the neighbourhood of the user ordered by date
        posts = BlogView.objects.filter(neighbourhood=neighbourhood).order_by("-created_at")
        return render(request, "posts.html", {"posts": posts})

def posts(request):
    current_user = request.user
    # get current user neighbourhood
    profile = Theprofile.objects.filter(user_id=current_user.id).first()
    # check if user has neighbourhood
    if profile is None:
        profile = Theprofile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = BlogView.objects.filter(user_id=current_user.id)
        # get all locations
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        category = Mycategory.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        # redirect to profile with error message
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighbourhood = profile.neighbourhood
        # get all posts in the neighbourhood of the user ordered by date
        posts = BlogView.objects.filter(neighbourhood=neighbourhood).order_by("-created_at")
        return render(request, "posts.html", {"posts": posts})