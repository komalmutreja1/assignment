from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class AuthTestSetUp(APITestCase):

    def setUp(self):
        self.registeration_url = reverse('register')
        self.login_url = reverse('login')

        # faker python module to generate dummy data
        self.fake_data = Faker()

        # valid user data
        self.user_test_data = {
            "username": self.fake_data.name().lower().split()[0],
            "password": self.fake_data.password(),
            "first_name": self.fake_data.name().split()[0],
            "last_name": self.fake_data.name().split()[-1]
        }

        # invalid user data
        self.user_invalid_data = {
            'first_name': 'my name',
            'password': '123'
        }

        return super().setUp()


    def tearDown(self):
        return super().tearDown()