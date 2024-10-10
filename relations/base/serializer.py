from rest_framework import serializers
from .models import Category,Product

class CategorySerializer (serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['name','id']

class ProductSerializer (serializers.ModelSerializer):
    category = CategorySerializer(required=False,allow_null=True)
    
    class Meta :
        model = Product
        # fields = '__all__'
        fields = ['id','name','description','price','category']
        # exclude=['category']
        