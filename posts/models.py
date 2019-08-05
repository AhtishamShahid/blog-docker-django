from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    post_image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=datetime.now)

    class Meta:
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.text
