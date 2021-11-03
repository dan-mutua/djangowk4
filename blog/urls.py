
from django.urls import path
from .views import HomePage, ProfilV, UpdateProfile




urlpatterns = [
  path('', HomePage.as_view(), name='home'),
  path('profile/<int:pk>', ProfilV.as_view(), name='profileV' ),
  path('updateprofile/<int:pk>',UpdateProfile.as_view(), name='updateprofile'),
  path('blog/edit/<int:pk>', UpdateProfile.as_view(), name="updateb"),
  
  
]


