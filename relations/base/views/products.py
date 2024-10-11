from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Product,Category
from ..serializer import ProductSerializer

fields = ['name','description','price','quantity']

@api_view(['GET','POST'])
def get_create_products(req:Request):
    pass
    if req.method =='GET':
        product = Product.objects.select_related('category').prefetch_related('suppliers').all()
        data = ProductSerializer(product,many=True)
        return Response(data.data,status.HTTP_200_OK)
        
    
    if req.method=='POST':
        print(req.data)
        serializer = ProductSerializer(data=req.data)
        if serializer.is_valid():
            supplier_id = serializer.validated_data.pop('suppliers_id')
            # products = Product.objects.create(**serializer.validated_data)
            products = serializer.save()
        
            # products.suppliers.set(supplier_id)
            products.suppliers.add(*supplier_id)
            return Response({"data":serializer.validated_data,"details":'Products created'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET',"PUT",'DELETE'])
def get_update_delete_product(req:Request,id):
        try:
           pk = int(id)
        except ValueError:
           return Response({'detail': 'ID should be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
       
        try:
            product = Product.objects.select_related('category').get(id=pk)
            if req.method =='GET':
                data = ProductSerializer(product)
                return Response(data.data,status.HTTP_200_OK)
        
            #  updating category here 
            if req.method=='PUT':
                for field in fields:
                    val = req.data.get(field)
                    if val is not None:
                        # print()
                        setattr(product,field,val)
                #         # pass
                        
                        # product[field] = val
                # name = req.data.get('name')
                # description = req.data.get('description')
                category = req.data.get('category')
                # price = req.data.get('price')
                # qty = req.data.get('quantity')
                # if name is not None:
                #     product.name = name
                # if description is not None:
                #     product.description = description  
                # if price is not None:
                #     product.price = description      
                if category is not None:
                    try:
                        category = Category.objects.get(id=category)  
                        product.category = category  
                    except Category.DoesNotExist:
                        return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)

                    product.category = category  
                
                if req.data is not None:
                    product.save()
                    return Response({"name":product.name,"description":product.description}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"details":"enter name or description"}, status=status.HTTP_400_BAD_REQUEST)
            
            if req.method=='DELETE':
                product.delete()
                return Response({"data":'Product deleted'},status.HTTP_200_OK)
        # throw an error if product does not exist 
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)   
    