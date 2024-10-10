from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Student
from ..serializer import StudentSerializer

@api_view(['GET','POST'])
def get_create_student(req:Request):
    if req.method =='GET':
        students = Student.objects.all()
        data = StudentSerializer(students,many=True)
        return Response(data.data,status.HTTP_200_OK)
        
    
    if req.method=='POST':
        print(req.data)
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.validated_data,"details":'student created'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)