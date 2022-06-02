import email
from email.policy import default
from math import fabs
from random import choices
from secrets import choice
from django.db import models
from django.forms import CharField

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20,null=False)
    sex = models.CharField(max_length=6, choices=(('male','男'),('female','女')), default='male')
    birth = models.DateField()
    email = models.EmailField(blank=True,default='')
    phone = models.CharField(max_length=15,blank=True,default='')

    def __str__(self):
        return self.name

class score(models.Model):
    sname = models.CharField(max_length=20,null=False,default="0")
    chinese = models.CharField(max_length=3,null=False,default="0")
    math = models.CharField(max_length=3,null=False,default="0")
    english = models.CharField(max_length=3,null=False,default="0")
    nature = models.CharField(max_length=3,null=False,default="0")
    
    def __str__(self):
        return self.sname