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
]
