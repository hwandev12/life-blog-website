from django.db import models
from django.urls import reverse

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog Post'
        
    header = models.CharField(max_length=200)
    text = models.TextField(max_length=300)
    slug =models.SlugField(unique=True)
    link = models.CharField(max_length=70)
    
    def __str__(self):
        return self.header
    
    def get_absolute_url(self):
        return reverse("blog:details", kwargs={'slug': self.slug})