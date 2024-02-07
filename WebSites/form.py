from django import forms

from blog.models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "slug",
            "author",
            "published",
            "description",
        ]
        labels = {"title": "Titre",
                 "slug": "Slug", "author": "auteur"} #modifier les champs
