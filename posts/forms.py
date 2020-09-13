from django import forms
from .models import Post

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'reading', 'image', 'body', 'status', 'tags']

class SearchForm(forms.Form):
    query = forms.CharField()