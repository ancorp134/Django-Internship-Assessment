from pickle import TRUE
from .models import Record
from .serializer import RecordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def Record_Details(request):
    
    if request.method =='GET':
        data=Record.objects.all()
        serializer=RecordSerializer(data,many=TRUE)
        return Response(serializer.data)
    
    
@api_view(['POST'])
def Add_Record(request):

    if request.method =='POST':
        serializer=RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
