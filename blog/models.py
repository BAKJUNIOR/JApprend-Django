from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def number_of_words(self):
        return len(self.description.split())

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug})













