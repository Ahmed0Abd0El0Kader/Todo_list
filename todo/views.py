from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from . models import *
from django.contrib.auth.mixins import LoginRequiredMixin # To Protect My Actions im website





# Create your views here.
def home(request):
    return render(request,'home.html')

class TaskList(LoginRequiredMixin,ListView): 
    model = Task         # Equal to tasks = Task.objects.all()    # In ListView class We Define the model object here which Model class We Want to view  
    context_object_name = 'tasks'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)
        return context
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    
    def get_queryset(self):
        base_qs = super(TaskDetail,self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks') 
    
    def get_queryset(self):
        base_qs = super(TaskUpdate,self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    def form_valid(self, form) :
        form.instance.user = self.request.user
        messages.success(self.request,"Task created successfully")
        return super(TaskUpdate,self).form_valid(form)   

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks') 
    
    def get_queryset(self):
        base_qs = super(TaskCreate,self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    
    def form_valid(self, form) :
        form.instance.user = self.request.user
        messages.success(self.request,"Task updated successfully")
        return super(TaskCreate,self).form_valid(form)   


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks') 
    
    def get_queryset(self):
        base_qs = super(TaskDelete,self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    def form_valid(self, form) :
        messages.success(self.request,"Task deleted successfully")
        return super(TaskDelete,self).form_valid(form)   #type: ignore