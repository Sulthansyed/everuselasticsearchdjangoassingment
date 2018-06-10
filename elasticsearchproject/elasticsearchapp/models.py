from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    distance = models.FloatField(blank=True,null=True)
    consume = models.FloatField(blank=True,null=True)
    speed = models.IntegerField(blank=True,null=True)
    temp_inside = models.FloatField(blank=True,null=True)
    temp_outside= models.FloatField(blank=True,null=True)
    specials= models.CharField(max_length=200,blank=True,null=True)
    gas_type=models.CharField(max_length=200,blank=True,null=True)
    AC=models.IntegerField(blank=True,null=True)
    rain=models.IntegerField(blank=True,null=True)
    sun=models.IntegerField(blank=True,null=True)
    














   
