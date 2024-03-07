from django.urls import path

from .views import TodoApiListView, TodoListView, TodoDetailApiView

urlpatterns = [
    # Traditional Django Views
    path('', TodoListView.as_view(), name='todo_list'),


    # Api Views
    path('todo_api/', TodoApiListView.as_view(), name='todo_list_api'),
    path('todo_api/<int:pk>/', TodoDetailApiView.as_view(), name='todo_detail_api'),
]
