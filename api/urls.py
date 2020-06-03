from django.urls import path, include 
from . import views


urlpatterns = [
    path('',views.apiOverView,name='api-overview'),
    path('task-list/',views.taskList,name='task-list'),
    path('task-detail/<str:pk>/',views.taskDetail,name='task-detail'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('taksk-update/<str:pk>/',views.taskUpdate,name='task-update'),
]
