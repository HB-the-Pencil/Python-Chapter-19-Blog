"""Define the blog URL paths."""

from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    # Home page.
    path("", views.index, name="index"),
    # List of blogs.
    path("blogs/", views.blogs, name="blogs"),
    # Path to an individual blog.
    path("blogs/<int:blog_id>", views.blog, name="blog"),
    # Path to add a new blog.
    path("new_blog/", views.new_blog, name="new_blog"),
    # Path to add a new blog post.
    path("new_post/<int:blog_id>", views.new_post, name="new_post"),
    # Path to edit a blog post.
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
]
