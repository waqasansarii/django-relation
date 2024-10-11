from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Product,Category,Supplier
from ..serializer import ProductSerializer,SupplierSerializer

fields = ['name','description','price','quantity','category']

@api_view(['GET','POST'])
def get_create_supplier(req:Request):
    pass
    if req.method =='GET':
        supplier = Supplier.objects.all()
        data = SupplierSerializer(supplier,many=True)
        return Response(data.data,status.HTTP_200_OK)
        
    
    if req.method=='POST':
        print(req.data)
        serializer = SupplierSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.validated_data,"details":'supplier created'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET',"PUT",'DELETE'])
def get_update_delete_supplier(req:Request,id):
        try:
           pk = int(id)
        except ValueError:
           return Response({'detail': 'ID should be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
       
        try:
            supplier = Supplier.objects.get(id=pk)
            if req.method =='GET':
                data = SupplierSerializer(supplier)
                return Response(data.data,status.HTTP_200_OK)
        
            #  updating supplier here 
            if req.method=='PUT':

                name = req.data.get('name')
                number = req.data.get('number')
                email = req.data.get('email')

                if name is not None:
                    supplier.name = name
                if number is not None:
                    supplier.number = number 
                if email is not None:
                    supplier.number = number      
            
                if req.data is not None:
                    supplier.save()
                    return Response({"name":supplier.name,"number":supplier.number}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"details":"enter name or number"}, status=status.HTTP_400_BAD_REQUEST)
            
            if req.method=='DELETE':
                supplier.delete()
                return Response({"data":'Supplier deleted'},status.HTTP_200_OK)
        # throw an error if product does not exist 
        except Supplier.DoesNotExist:
            return Response({'detail': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)   
    