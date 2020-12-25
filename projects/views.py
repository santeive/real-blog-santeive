from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, "projects/projects.html")

