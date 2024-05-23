import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import User, Project, Task, Tag

class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('user-list')

    def test_list_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user(self):
        data = {'username': 'testuser2', 'email': 'test2@example.com', 'password': '12345'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

class ProjectViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='projectuser', password='12345', email='project@example.com')
        self.client.login(username='projectuser', password='12345')
        self.url = reverse('project-list')

    def test_list_projects(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_project(self):
        data = {'name': 'Project1', 'description': 'Description1'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='taskuser', password='12345', email='task@example.com')
        self.client.login(username='taskuser', password='12345')
        self.project = Project.objects.create(name='Project2', description='Description2', creator=self.user)
        self.tag = Tag.objects.create(title='Tag1')
        self.url = reverse('task-list')

    def test_list_tasks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_task(self):
        data = {'title': 'Task1', 'description': 'Task Description', 'project': self.project.id, 'tags': [self.tag.id]}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

class TagViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='taguser', password='12345', email='tag@example.com')
        self.client.login(username='taguser', password='12345')
        self.url = reverse('tag-list')

    def test_list_tags(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_tag(self):
        data = {'title': 'Tag1'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)

if __name__ == '__main__':
    unittest.main()
