# Django
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Third Party
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    READING_CHOICES = (
        ('5 minutes', '5 Minutes' ),
        ('10 minutes', '10 Minutes'),
        ('20 minutes', '20 Minutes'),
        ('30 minutes', '30 Minutes')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    reading = models.CharField(max_length=20, choices=READING_CHOICES, default='5 minutes')
    image = models.ImageField(upload_to='posts', blank=True)
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # Helps to create a canonical URL
    def get_absolute_url(self):
        return reverse('posts:post_detail', 
                        args=[self.publish.year, 
                              self.publish.month, 
                              self.publish.day, self.slug])

