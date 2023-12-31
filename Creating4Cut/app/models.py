from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to='images/', blank=True, null=True)