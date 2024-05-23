import unittest
from django.test import TestCase
from core.models import User, Project, Task, Tag

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='projectuser', password='12345', email='project@example.com')
        self.project = Project.objects.create(name='Project1', description='Description1', creator=self.user)

    def test_project_creation(self):
        self.assertEqual(self.project.name, 'Project1')
        self.assertEqual(self.project.description, 'Description1')
        self.assertEqual(self.project.creator, self.user)

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='taskuser', password='12345', email='task@example.com')
        self.project = Project.objects.create(name='Project2', description='Description2', creator=self.user)
        self.task = Task.objects.create(title='Task1', description='Task Description', project=self.project)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Task1')
        self.assertEqual(self.task.description, 'Task Description')
        self.assertEqual(self.task.project, self.project)

class TagTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(title='Tag1')

    def test_tag_creation(self):
        self.assertEqual(self.tag.title, 'Tag1')

if __name__ == '__main__':
    unittest.main()
