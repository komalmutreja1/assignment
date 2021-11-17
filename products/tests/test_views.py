from products.tests.test_setup import ProductTestSetUp
from rest_framework.test import APIClient





class TestViews(ProductTestSetUp):

    def test_user_cannot_perform_operations_on_products_without_authentication(self):
        """
        This test ensures that unauthenticated user can not perform any operation on products.
        API will return 401 UnAuthorized error message to user.
        """
        post_response = self.client.post(self.product_url, self.product_mobile_test_data, format="json")
        get_response = self.client.get(self.product_url)

        self.assertEqual(post_response.status_code, 401)
        self.assertEqual(get_response.status_code, 401)


    def test_user_cannot_create_product_with_invalid_data(self):
        """
        This test ensures that authenticated user can not create a product with invalid or incomplete data.
        API will return 400 with an appropriate error message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_response = client.post(self.product_url, self.product_invalid_data, format="json")

        self.assertEqual(product_response.status_code, 400)


    def test_user_cannot_create_mobile_product_without_additional_required_attributes(self):
        """
        This test ensures that authenticated user can not create a product with type Mobile without required 
        additional attributes for Mobile ie screen_size and color.
        API will return 400 with a required fields error message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_response = client.post(self.product_url, self.product_mobile_invalid_data, format="json")

        self.assertEqual(product_response.status_code, 400)


    def test_user_cannot_create_laptop_product_without_additional_required_attributes(self):
        """
        This test ensures that authenticated user can not create a product with type Laptop without required 
        additional attributes for Laptop ie. hd_capacity.
        API will return 400 with a required fields error message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_response = client.post(self.product_url, self.product_laptop_invalid_data, format="json")

        self.assertEqual(product_response.status_code, 400)


    def test_user_can_create_mobile_product_with_valid_data(self):
        """
        This test ensures that authenticated user can create a product with valid and complete required additional 
        attributes data for type Mobile.
        API will return 201 with success message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_response = client.post(self.product_url, self.product_mobile_test_data, format="json")

        self.assertEqual(product_response.status_code, 201)


    def test_user_can_create_laptop_product_with_valid_data(self):
        """
        This test ensures that authenticated user can create a product with valid and complete required additional 
        attributes data for type Laptop.
        API will return 201 with success message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_response = client.post(self.product_url, self.product_laptop_test_data, format="json")

        self.assertEqual(product_response.status_code, 201)


    def test_user_cannot_update_nonexistent_product_or_product_with_invalid_id(self):
        """
        This test ensures that authenticated user can not update an invalid or nonexistent product.
        API will return 400 with Invalid or Void id for product, message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_post_response = client.post(self.product_url, self.product_laptop_test_data, format="json")
        data_to_be_updated = {
            'id': None,
            'name': 'updated product name'
        }
        product_put_response = client.put(self.product_url, data_to_be_updated, format="json")

        self.assertEqual(product_put_response.status_code, 400)


    def test_user_can_update_product_with_valid_id(self):
        """
        This test ensures that authenticated user can update a valid product with valid data.
        API will return 200 with success message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_post_response = client.post(self.product_url, self.product_laptop_test_data, format="json")

        data_to_be_updated = {
            'id': product_post_response.data.get('data').get('id'),
            'name': 'updated product name'
        }
        product_put_response = client.put(self.product_url, data_to_be_updated, format="json")

        self.assertEqual(product_put_response.status_code, 200)


    def test_user_cannot_delete_nonexistent_product_or_product_with_invalid_id(self):
        """
        This test ensures that authenticated user can not delete an invalid or nonexistent product.
        API will return 400 with Invalid or Void id for product, message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_post_response = client.post(self.product_url, self.product_laptop_test_data, format="json")

        product_delete_response = client.delete(f"{self.product_url}?id=None")

        self.assertEqual(product_delete_response.status_code, 400)


    def test_user_can_delete_product_with_valid_id(self):
        """
        This test ensures that authenticated user can delete a valid product.
        API will return 200 with success message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_post_response = client.post(self.product_url, self.product_laptop_test_data, format="json")

        product_delete_response = client.delete(f"{self.product_url}?id={product_post_response.data.get('data').get('id')}")

        self.assertEqual(product_delete_response.status_code, 200)


    def test_authenticated_user_can_fetch_all_products(self):
        """
        This test ensures that authenticated user can fetch all products.
        API will return 200 with success message to user.
        """
        registration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")
        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + login_response.data.get('data').get('token'))
        product_laptop_response = client.post(self.product_url, self.product_laptop_test_data, format="json")
        product_mobile_response = client.post(self.product_url, self.product_mobile_test_data, format="json")
        product_get_response = client.get(self.product_url)

        self.assertEqual(product_get_response.status_code, 200)
