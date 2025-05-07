from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


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


@login_required
def new_blog(request):
    """Create a new blog."""
    if request.method != "POST":
        # Create a new form if it's not being submitted.
        form = BlogForm()
    else:
        # Submit data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blogs")

    # Display the form.
    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def new_post(request, blog_id):
    """Create a new post for a blog."""
    blog = Blog.objects.get(id=blog_id)
    if request.method != "POST":
        # Create a new form if it's not being submitted.
        form = BlogPostForm()
    else:
        # Submit data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect("blogs:blog", blog_id=blog_id)

    context = {"blog": blog, "form": form}
    return render(request, "blogs/new_post.html", context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    if request.method != "POST":
        # Fill the form with the existing information.
        form = BlogPostForm(instance=post)
    else:
        # Submit data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog", blog_id=blog.id)

    context = {"post": post, "blog": blog, "form": form}
    return render(request, "blogs/edit_post.html", context)
