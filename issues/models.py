from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Issues(models.Model):
    """"single issue"""
    
    name = models.CharField(max_length=200, blank=False)
    summary = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tag= models.CharField(max_length=30, blank=True, null=True)
    image= models.ImageField(upload_to="img",blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    

    
    def __unicode__(self):
        return self.title
# Create your models here.
