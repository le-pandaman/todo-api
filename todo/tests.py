from django.test import TestCase
from django.urls import reverse

from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

from .models import Todo


class TodoListView(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.todo = Todo.objects.create(
            task='hello',
            is_done=False,
            date=datetime.now(),
            completed=datetime.now(),
        )

    def test_todo_list_view(self):

        response = self.client.get(reverse('todo_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)

    def test_todo_list_template(self) -> None:

        response = self.client.get(reverse('todo_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        self.assertContains(response, 'hello')


class TodoAPIListView(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.todo = Todo.objects.create(
            task='hello',
            is_done=False,
            date=datetime.now(),
            completed=datetime.now()
        )

    def test_todo_listview_status(self) -> None:

        response = self.client.get(reverse('todo_list_api'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_list_view_object_count(self) -> None:

        response = self.client.get(reverse('todo_list_api'))

        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_todo_list_detail_view(self) -> None:

        response = self.client.get(
            reverse('todo_detail_api', kwargs={'pk': self.todo.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'hello')
        self.assertEqual(response.data['is_done'], False)
