from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('tasks/',views.TaskList.as_view(template_name='task_list.html'),name='tasks'),
    path('task/<int:pk>/',views.TaskDetail.as_view(template_name='todo/task_detail.html'),name='task'),
    path('task/create/',views.TaskCreate.as_view(template_name='todo/task_form.html'),name='task-create'),
    path('task/update/<int:pk>/',views.TaskUpdate.as_view(),name='task-update'),
    path('task/delete/<int:pk>/',views.TaskDelete.as_view(template_name='todo/task_confirm_delete.html'),name='task-delete'),
]
