from rest_framework.decorators import api_view
from .models import ModelTasks
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def tasks_list(request):
    if request.method == 'GET':
        data = ModelTasks.objects.all()
        serializer = TasksSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET','PUT','PATCH'])
def edit_task(request,id):
    mydata = ModelTasks.objects.get(id=id)
    if request.method == 'GET':
        serializer = TasksSerializer(mydata)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TasksSerializer(mydata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TasksSerializer(mydata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mydata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)