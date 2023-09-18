from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# from .models import 
# from .views import
# from members.models import MemberModel
# from members.views import MemberView

class MyBlogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_my_model(self):
        self.assertEqual(self.my_model_instance.title, "Test Post")
        self.assertEqual(self.my_model_instance.content, "Test Content")
        self.assertEqual(self.my_model_instance.author, self.user)



class MembersTestCase(TestCase):
    def test_member_model(self):
        member = MemberModel.objects.create(name="Test Member", email="test@example.com")

        self.assertEqual(member.name, "Test Member")
        self.assertEqual(member.email, "test@example.com")
