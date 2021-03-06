from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="unittester", email="test@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            name="chips", description="I love chips", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'chips')