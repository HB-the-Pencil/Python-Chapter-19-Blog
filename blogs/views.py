from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    """The home page for the blog website."""
    return render(request, "blogs/index.html")


def blogs(request):
    """Show a list of blogs."""
    blogs = Blog.objects.order_by("-date_added")
    context = {"blogs": blogs}
    return render(request, "blogs/blogs.html", context)


def blog(request, blog_id):
    """Show an individual blog and its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.order_by("-date_added")
    context = {"blog": blog, "posts": posts}
    return render(request, "blogs/blog.html", context)