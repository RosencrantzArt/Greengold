from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=169, unique=True)
    slug = models.SlugField(max_length=169, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_post", blank=True)
    excerpt = models.TextField(default="")
       
    def total_likes(self):
        return self.likes.count()

    def is_published(self):
        return self.status == 1

    def __str__(self):
        return self.title


class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
def __str__(self):
        return f"Comment by {self.author} on {self.post}"
