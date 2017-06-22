import unittest

from User import User


class TestUser(unittest.TestCase):
    """
        Class performing unit testing for class User
    """

    # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.user = User()

    # defining method to test for creating user account
    def test_create_account(self):
        self.user.users = {}
        res = self.user.create_account('ian', 'email@mail.com', 'ian', 'ian')
        self.assertEqual({'email@mail.com': {'pass': 'ian', 'name': 'ian', 'email': 'email@mail.com'}}, res,
                         "Output should be {'email@mail.com': {'pass': 'ian', 'name': 'ian', 'email': "
                         "'email@mail.com'}}")

    # defining method to test creating account with empty name field
    def test_create_account_empty_name(self):
        self.user.users = {}
        res = self.user.create_account('', 'email@mail.com', 'ian', 'ian')
        self.assertEqual({'error': 'Fill all Fields'}, res,
                         "Output should be {'error': 'Fill all Fields'}")

    # defining method to test creating account with password name field
    def test_create_account_empty_password(self):
        self.user.users = {}
        res = self.user.create_account('ian', 'email@mail.com', '', 'ian')
        self.assertEqual({'error': 'Fill all Fields'}, res,
                         "Output should be {'error': 'Fill all Fields'}")

    # defining method to test creating account with non matching password and confirm password
    def test_create_account_not_matching_password(self):
        self.user.users = {}
        res = self.user.create_account('ian', 'email@mail.com', 'ian', 'iano')
        self.assertEqual({'error': 'Password Mismatch'}, res,
                         "Output should be {'error': 'Password Mismatch'}")

    # defining method to test login with wrong credentials
    def test_wrong_login(self):
        self.user.users = {}
        self.user.create_account('ian', 'email@mail.com', 'ian', 'ian')
        login = self.user.login('email@mail.com', 'ian123')
        self.assertEqual(login, {'error': 'Incorrect Login'}, "Output should be {'error': 'Incorrect Login'}")

    # defining method to test creating existing account
    def test_create_existing_user_account(self):
        self.user.users = {}
        res = self.user.create_account('ian', 'email@mail.com', 'ian', 'ian')
        res = self.user.create_account('ian', 'email@mail.com', 'ian', 'ian')
        expect = {'error': 'User already Exist. Please Login'}
        self.assertEqual(res, expect, "Output should be expect = {'error': 'User already Exist. Please Login'}")

    # defining method to test deleting user account
    def test_delete_user_account(self):
        self.user.users = {}
        res = self.user.create_account('ian', 'email@mail.com', 'ian', 'ian')
        res = self.user.del_account('email@mail.com')
        expect = {'success': 'You have successfully deleted your account'}
        self.assertEqual(res, expect, "Output should be {'success': 'You have successfully deleted your account'}")

    # defining method to test login with empty password and empty email address
    def test_login_with_empty_fields(self):
        res = self.user.login('', '')
        expect = {'error': 'Fill all Fields'}
        self.assertEqual(res, expect, "Output should be {'error': 'Fill all Fields'}")


if __name__ == "__main__":
    unittest.main()
