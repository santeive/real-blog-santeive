from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('/about', views.about, name="about"),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name="post_detail"),
]