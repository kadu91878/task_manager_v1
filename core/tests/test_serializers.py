import unittest
from rest_framework.exceptions import ValidationError
from core.serializers import UserSerializer, ProjectSerializer, TaskSerializer, TagSerializer
from core.models import User, Project, Task, Tag

class UserSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_data = {'username': 'testuser', 'email': 'test@example.com', 'password': '12345'}
        self.invalid_data = {'username': '', 'email': 'test@example.com', 'password': '12345'}
    
    def test_serializer_with_valid_data(self):
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_with_invalid_data(self):
        serializer = UserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_serializer_save(self):
        serializer = UserSerializer(data=self.valid_data)
        if serializer.is_valid():
            user = serializer.save()
            self.assertEqual(user.username, 'testuser')

class ProjectSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='projectuser', password='12345', email='project@example.com')
        self.valid_data = {'name': 'Project1', 'description': 'Description1', 'creator': self.user.id}
        self.invalid_data = {'name': '', 'description': 'Description1', 'creator': self.user.id}

    def test_serializer_with_valid_data(self):
        serializer = ProjectSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_with_invalid_data(self):
        serializer = ProjectSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_serializer_save(self):
        serializer = ProjectSerializer(data=self.valid_data)
        if serializer.is_valid():
            project = serializer.save()
            self.assertEqual(project.name, 'Project1')

class TaskSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='taskuser', password='12345', email='task@example.com')
        self.project = Project.objects.create(name='Project2', description='Description2', creator=self.user)
        self.tag = Tag.objects.create(title='Tag1')
        self.valid_data = {'title': 'Task1', 'description': 'Task Description', 'project': self.project.id, 'tags': [self.tag.id]}
        self.invalid_data = {'title': 'Task1', 'description': 'Task Description', 'project': self.project.id, 'tags': []}

    def test_serializer_with_valid_data(self):
        serializer = TaskSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_with_invalid_data(self):
        serializer = TaskSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('tags', serializer.errors)

    def test_serializer_save(self):
        serializer = TaskSerializer(data=self.valid_data)
        if serializer.is_valid():
            task = serializer.save()
            self.assertEqual(task.title, 'Task1')

class TagSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_data = {'title': 'Tag1'}
        self.invalid_data = {'title': ''}

    def test_serializer_with_valid_data(self):
        serializer = TagSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_with_invalid_data(self):
        serializer = TagSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_serializer_save(self):
        serializer = TagSerializer(data=self.valid_data)
        if serializer.is_valid():
            tag = serializer.save()
            self.assertEqual(tag.title, 'Tag1')

if __name__ == '__main__':
    unittest.main()
