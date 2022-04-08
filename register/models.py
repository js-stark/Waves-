from atexit import register
from operator import mod
from django.db import models
from waves_events.models import Event
from accounts.models import Account

# Create your models here.


class Register(models.Model):

    register_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.register_id

class RegisterItem(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    register = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.event.price

    def __unicode__(self):
        return self.event