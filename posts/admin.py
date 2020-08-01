from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # En Admin: Muestra los post de la seguiente manera
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Crea una barra lateral con los siguientes filtros
    list_filter = ('status', 'created', 'publish', 'author')
    # Crea un buscador para titulo y body
    search_fields = ('title', 'body')
    # Autocompleta el campo slug de acuerdo con el titulo
    prepopulated_fields = {'slug': ('title',)}
    # Links de navegación por fecha
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    # Ordena de acuerdo al estado de la publicacion
    ordering = ('status', 'publish')
