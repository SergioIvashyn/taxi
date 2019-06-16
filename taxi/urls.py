from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name='index'),
	path('accounts/profile/', profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='taxi/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='taxi/logout.html'), name='logout'),
]
