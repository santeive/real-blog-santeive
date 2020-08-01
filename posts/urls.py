from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name="post_detail"),
]