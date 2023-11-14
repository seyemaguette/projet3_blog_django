from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Article (models.Model):
    title = models.CharField( max_length=150)
    summary = models.CharField( max_length=500)
    content = RichTextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    archive = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['-creation_date']


    def __str__(self):
        return f"{self.title}"

    