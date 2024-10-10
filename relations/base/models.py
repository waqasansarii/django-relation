from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    bio = models.TextField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    
