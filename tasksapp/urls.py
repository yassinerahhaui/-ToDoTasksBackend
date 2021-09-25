from django.urls import path
from .views import tasks_list,edit_task

app_name='tasks'

urlpatterns = [
    path('get-list/',tasks_list,name='list'),
    path('get-list/<int:id>/',edit_task,name='edit'),
]
