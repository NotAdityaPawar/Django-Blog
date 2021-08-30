from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length=255, default="title tag")
    body = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list')
