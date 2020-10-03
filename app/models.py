from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    location = models.CharField(max_length=300)
    distance = models.FloatField()
    time = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']
