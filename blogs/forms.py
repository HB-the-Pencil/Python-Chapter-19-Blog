from django import forms
from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["text"]
        labels = {"text": ""}