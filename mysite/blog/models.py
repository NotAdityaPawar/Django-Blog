from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)