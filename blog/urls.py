from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import UserRegister, UserEdit

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('search/', views.search_businesses, name='search_results'),
    path('business/(\d+)', views.get_business, name='business_results'),
    path('new/business', views.business, name='business'),
    path('new/post', views.new_post, name='new_post'),
    path('logout/', views.logout, name='logout'),
    

    path('register/', UserRegister.as_view(), name='signup'),
    path('edit_profile/',  UserEdit.as_view(), name='edit_profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)