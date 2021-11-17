from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class ProductTestSetUp(APITestCase):

    def setUp(self):
        self.registeration_url = reverse('register')
        self.login_url = reverse('login')
        self.product_url = reverse('products')


        # faker python module to generate dummy data
        self.fake_data = Faker() 

        # valid product mobile data
        self.product_mobile_test_data = {   
            "name": "SamSung",
            "description": "this is Samsung mobile",
            "processor": "mediatek G 930",
            "type": "Mobile",
            "ram": "8 GB",
            "screen_size": "5.6",
            "color": "blue"
        }

        # invalid product mobile data, as it does not have other required attributes 
        # for mobile ie. screen_size, color
        self.product_mobile_invalid_data = {
            "name": "SamSung",
            "description": "this is Samsung mobile",
            "processor": "mediatek G 930",
            "type": "Mobile",
            "ram": "8 GB"
        }

        # valid product laptop data
        self.product_laptop_test_data = {
            "name": "Lenovo",
            "description": "this is a Lenovo laptop",
            "processor": "i5 8th gen",
            "type": "Laptop",
            "ram": "16 GB",
            "hd_capacity": "1 TB"
        }

        # invalid product laptop data, as it does not have other required attributes 
        # for laptop ie. hd_capacity
        self.product_laptop_invalid_data = {
            "name": "Lenovo",
            "description": "this is a Lenovo laptop",
            "processor": "i5 8th gen",
            "type": "Laptop",
            "ram": "16 GB"
        }
        
        # invalid product data
        self.product_invalid_data = {
            'name': 'my product name',
            'color': 'yellow'
        }

        # valid user data
        self.user_test_data = {
            "username": self.fake_data.name().lower().split()[0],
            "password": self.fake_data.password(),
            "first_name": self.fake_data.name().split()[0],
            "last_name": self.fake_data.name().split()[-1]
        }

        return super().setUp()


    def tearDown(self):
        return super().tearDown()