from django.db import models
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Add_Comment(models.Model):
    comment = models.TextField(max_length=500 , default='nothing' , blank=True)
    writer = models.ForeignKey(User , default = None , on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comment


class Report_Issue(models.Model):
    issue = models.TextField(max_length=500 , default='nothing' , blank=True)
    writer = models.ForeignKey(User , default = None , on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Mystry_and_Police(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information =models.TextField(blank=True)
    pdf_file = models.FileField(default='' , blank=True)

    def __str__(self):
        return self.name


class Sciences(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information =models.TextField(blank=True)
    pdf_file = models.FileField(default='' , blank=True)
    

    def __str__(self):
        return self.name


class Programming(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information =models.TextField(blank=True)
    pdf_file = models.FileField(default='' , blank=True)
    
    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information =models.TextField(blank=True)
    pdf_file = models.FileField(default='' , blank=True)
    
    def __str__(self):
        return self.name


class Islam(models.Model):    
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information = models.FileField(default='' , blank=True)
    pdf_file = models.FileField(default='' , blank=True)
    

    def __str__(self):
        return self.name

    def __str__(self):
        return self.auther


class Psychology(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    auther = models.CharField(max_length=200 , blank=True)
    story = models.TextField(blank=True)
    information =models.TextField(blank=True)
    pdf_file = models.FileField(default='' , blank=True)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True)
    user = models.ForeignKey(User,null = True, on_delete = models.CASCADE) 
    completed =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)