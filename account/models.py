from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'