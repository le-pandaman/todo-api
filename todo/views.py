from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


# Traditional views

class TodoListView(ListView):

    model = Todo
    context_object_name = 'todos'
    template_name = 'todo/todo_list.html'


# Api Views
class TodoApiListView(generics.ListAPIView):

    model = Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDetailApiView(generics.RetrieveAPIView):

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
