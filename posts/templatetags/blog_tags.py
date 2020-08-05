 
from django.utils.safestring import mark_safe
import markdown
from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('posts/lastest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('posts/tags_used.html')
def total_tags():
    total_tags = Post.tags.all()
    return {'total_tags': total_tags}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))