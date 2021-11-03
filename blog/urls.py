
from django.urls import path
from .views import HomePage,DeleteViewB, NeibaD, UpdateProfile




urlpatterns = [
  path('', HomePage.as_view(), name='home'),
  path('neiba/<int:pk>', NeibaD.as_view(), name='neiba_detail' ),
  path('updateprofile/<int:pk>',UpdateProfile.as_view(), name='updateprofile'),
  path('blog/edit/<int:pk>', UpdateProfile.as_view(), name="updateb"),
  path('article/<int:pk>/delete',  DeleteViewB.as_view(), name="deleteb"),
  
]


