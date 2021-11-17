from accounts.tests.test_setup import AuthTestSetUp


class TestViews(AuthTestSetUp):
    def test_user_cannot_register_with_invalid_data(self):
        """
        This test ensures that user can not be registered with invalid or missing data.
        API will return 400 with an appropriate error message to user.
        """
        response = self.client.post(self.registeration_url, self.user_invalid_data, format="json")

        self.assertEqual(response.status_code, 400)


    def test_user_can_register_successfuly_with_valid_data(self):
        """
        This test ensures that user can be registered with valid valid and complete required data.
        API will return 201 with a success message to user.
        """
        response = self.client.post(self.registeration_url, self.user_test_data, format="json")

        self.assertEqual(self.user_test_data.get('username'), response.data.get('data').get('username'))
        self.assertEqual(self.user_test_data.get('first_name'), response.data.get('data').get('first_name'))
        self.assertEqual(self.user_test_data.get('last_name'), response.data.get('data').get('last_name'))
        self.assertEqual(response.status_code, 201)



    def test_user_cannot_login_with_invalid_credentials(self):
        """
        This test ensures that user can not be logged in with invalid or incomplete data.
        API will return 400 with an appropriate error messageto user.
        """
        registeration_response = self.client.post(self.registeration_url, self.user_test_data, format="json")

        login_response = self.client.post(self.login_url, {'username': 'invalid', 'password': 'xyz'}, format="json")

        self.assertEqual(login_response.status_code, 400)


    def test_user_can_login_with_valid_credentials(self):
        """
        This test ensures that user can be logged in with valid and complete required data.
        API will return 200 with a success message to user.
        """
        response = self.client.post(self.registeration_url, self.user_test_data, format="json")

        login_response = self.client.post(self.login_url, self.user_test_data, format="json")

        self.assertEqual(login_response.status_code, 200)
