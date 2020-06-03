from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'task-list',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/taksk-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serialiser = TaskSerializer(task,many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serialiser = TaskSerializer(task,many=False)
    return Response(serialiser.data)

@api_view(['POST'])
def taskCreate(request):
    serialiser = TaskSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serialiser = TaskSerializer(instance=task, data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item was Deleted')