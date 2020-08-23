from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .feeds import LastestPostsFeed

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create_article, name="create"),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('about/', views.about, name="about"),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name="post_detail"),
    path('feed/', LastestPostsFeed(), name='post_feed'),
]