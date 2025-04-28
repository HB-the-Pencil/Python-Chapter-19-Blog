from django.db import models

# Create your models here.
class Blog(models.Model):
    """Create a blog about a topic."""
    blog_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the name of the blog and its author."""
        return f"{self.blog_name} by {self.author}"


class BlogPost(models.Model):
    """Create a post for a blog."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"

    def __str__(self):
        """Return a truncated preview of the content."""
        return (
            f"{self.title}\n"
            f"{self.text[:50]}{"..." if len(str(self.text)) > 50 else ""}"
        )