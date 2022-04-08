from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Event(models.Model):

    event_name = models.CharField(max_length=200,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length = 2000, blank=True)
    rounds = models.TextField(max_length=2000,blank=True)
    rules = models.TextField(max_length=2000,blank=True)
    contact = models.TextField(max_length=500,blank=True)
    date = models.TextField(max_length=100,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/events')
    poster = models.ImageField(upload_to='photos/posters')
    is_updated = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()

    def __str__(self):

        return self.event_name
    
    def get_url(self):

        return reverse('event_detail',args=[self.category.slug,self.slug])