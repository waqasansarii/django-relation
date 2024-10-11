from rest_framework import serializers
from .models import Category,Product,Supplier

class CategorySerializer (serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['name','id','description']

class SupplierSerializer (serializers.ModelSerializer):
    class Meta :
        model = Supplier
        fields = ['name','id','number','email']



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    suppliers = SupplierSerializer(many=True,read_only=True)
    suppliers_id = serializers.ListField(write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'category','suppliers','category_id','suppliers_id']        
   