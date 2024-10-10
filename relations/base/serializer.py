from rest_framework import serializers
from .models import Category,Student

class CategorySerializer (serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'

class StudentSerializer (serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'
        