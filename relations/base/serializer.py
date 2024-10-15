from rest_framework import serializers
from .models import Category,Product,Supplier

class CategorySerializer (serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['name','id','description']

# for supplier 
class ProductSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'category']        


class SupplierSerializer (serializers.ModelSerializer):
    products = ProductSupplierSerializer(read_only=True,many=True,source='productsSupplier')
    # product_ids = serializers.ListField(write_only=True,allow_null=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
        write_only=True
    )
    class Meta :
        model = Supplier
        fields = ['name','id','number','email','products','product_ids']



#// for products serializera
class SupplierProductSerializer (serializers.ModelSerializer):
    class Meta :
        model = Supplier
        fields = ['name','id','number','email']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    suppliers = SupplierProductSerializer(many=True,read_only=True)
    suppliers_id = serializers.ListField(write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'category','suppliers','category_id','suppliers_id']        



# for reverse category data 
class ProductCategorySerializer(serializers.ModelSerializer):
    suppliers = SupplierProductSerializer(many=True,read_only=True,source='productsSupplier')
    
    class Meta:
        model= Product
        fields = ['id', 'name', 'description', 'price', 'quantity','suppliers']        
        
    
    
class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductCategorySerializer(read_only=True,many=True,source='productsCategory')
    # products = productsCategory 
    class Meta:
        model= Category
        fields = ['id', 'name', 'description', 'products' ]        
           