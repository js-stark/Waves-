from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.

class Team(models.Model):

    team_name = models.CharField(max_length=500)
    slug = models.SlugField()

    def __str__(self):

        return self.team_name

class Team_members(models.Model):

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    social_link_1 = models.CharField(max_length=500,blank=True)
    social_link_2 = models.CharField(max_length=500,blank=True)
    social_link_3 = models.CharField(max_length=500,blank=True)
    photo = models.ImageField(upload_to='photos/team')

    def __str__(self):

        return f'{self.name} -- {self.designation}'


