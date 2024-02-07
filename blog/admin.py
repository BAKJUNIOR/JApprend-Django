from django.contrib import admin

# Register your models here.
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'slug',
        'published',
        'date',
        'description',
        'number_of_words'
    )
    ordering = ('-published', '-date') # Trier les élements de la table
    list_editable = ("slug", "title", )#modifier directement un champs de la db
    list_display_links = ("author",)

    empty_value_display = 'Inconnu'

    search_fields = ('title', 'slug', )
    list_filter = ('published', 'author')

    autocomplete_fields = ('author', ) # un choix par selection
    filter_horizontal = ('category', ) # filter sur les champs maytomay
    list_per_page = 6#filter le nombre article a afficher