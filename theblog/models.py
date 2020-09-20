from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Issue(models.Model):
    name = models.CharField(max_length=255, default="Issue")
    title = models.CharField(max_length=255)
    parallaximage = models.ImageField(null=True,blank=True, upload_to="images/")
    color = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('issue')
    


    
class Post(models.Model):
    title = models.CharField(max_length=255)
    tab_title = models.CharField(max_length=255, default="A Golden Fern")

    author = models.CharField(max_length=255, default="Anonymous") 
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    issue_title = models.CharField(max_length=255, default="Issue")
    
    def __str__(self):
        return self.title + ' | '+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    

    
# Create your models here.