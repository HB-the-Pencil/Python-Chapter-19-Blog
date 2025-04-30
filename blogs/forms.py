from django import forms
from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["blog_name", "author"]
        labels = {"blog_name": "Blog Name", "author": "Author"}

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
        labels = {"title": "Title", "text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}