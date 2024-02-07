from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from WebSites.form import BlogForm
from blog.models import BlogPost


# Create your views here.



@login_required()
# @user_passes_test(lambda u: u.username == 'bak')
def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

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
    try:
        post = BlogPost.objects.get(slug=slug)
        return render(request, 'blog/post.html', context={'post': post})
    except BlogPost.DoesNotExist:
        # Si aucun objet BlogPost correspondant n'est trouvé, renvoyer une autre page HTML error
        return render(request, 'blog/error404.html')


def blogForm(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Blog post saved")
    else:
        form = BlogForm()

    return render(request, 'blog/blogForm.html', context={'form': form})
