from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null= True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True)
    
    
    
