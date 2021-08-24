from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title