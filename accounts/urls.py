"""Define URL paths for account information."""

from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    # Include the default authorization URLs.
    path("", include("django.contrib.auth.urls")),
    # Path to registration page.
    path("register/", views.register, name="register"),
]