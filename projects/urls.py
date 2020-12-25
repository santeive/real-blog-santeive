from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
app_name = 'projects'

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project', views.projects, name="project"),
]