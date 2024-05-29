from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import TaskSerializer
from .permissions import IsOwnerOnly
from todo.models import Task

# Create your views here.



class TodoList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
    def filter_queryset(self, queryset):
        queryset = queryset.filter(user = self.request.user)
        return super().filter_queryset(queryset)
        
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer        
        
        