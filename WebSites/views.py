from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the")

@login_required()
#@user_passes_test(lambda u: u.username == 'bak')
def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

    """
    blog_post = get_object_or_404(BlogPost, pk=2)
    return HttpResponse(blog_post.content)
    """
"""
  try:
        blog_post = BlogPost.objects.get(pk=5)
        return HttpResponse(blog_post.content)
   except BlogPost.DoesNotExist:
        return render(request, 'blog/error404.html')
"""


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post': post})