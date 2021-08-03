import unittest # Importing the unittest module
import pyperclip
from user import User
from credentials import Credential

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''    # Items up here .......

    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_user = User("Keem", "1234") 
    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name, "Keem")
        self.assertEqual(self.new_user.user_password, "1234")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into 
        the user list
        '''
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
         '''
         method to clean up after each test
         '''
         User.user_list = []
    def test_save_multiple_user(self):
        '''
        method to test multiple saved users
        '''
        self.new_user.save_user()
        test_user = User("Keem","1234",) 
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    def test_delete_user(self):
         """
         delete users
         """
         self.new_user.save_user()
         test_user = User("Keem", "1234") 
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.user_list), 1)
    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.user_list)
class TestCredentials (unittest.TestCase):
    def setUp(self):
        """
        define the constructor
        """
        self.cred = Credentials("Facebook", "----", "0000")
    def tearDown(self,parameter_list):
        """
        clear up during each test
        """
        pass
    def test_init(self):
        """
        make sure the constructor is well initialized
        """
        self.assertEqual(self.cred.accountName, "Facebook")
        self.assertEqual(self.cred.accountUsername, "..")
        self.assertEqual(self.cred.accountPassword, "1234")
    def test_save_multiples_cred(self):
        """
        test for multiple credentials
        """
        self.cred.saveCredential()
        test_cred = Credentials("Facebook", "....", 1234)  
        test_cred.saveCredential()
        self.assertEqual(len(Credentials.credentials), 3)
    def test_delete(self):
        """
        test if the credential can be deleted
        """
        self.cred.saveCredential()
        test_cred = Credentials("Facebook", "....", 0000)  
        test_cred.saveCredential()
        self.cred.deleteCredential()
        self.assertEqual(len(Credentials.credentials), 1)
    def test_search(self):
        """
        search a credential
        """
        self.cred.searchCredential()
        test_cred = Credentials("Facebook", "8888", 0000)  
        test_cred.searchCredential()
        found = Credentials.searchCredential("Facebook")
        self.assertEqual(found.accountName, test_cred.accountName)
    def test_display(self):
        """
        method to test if credentials can be displayed
        """
        self.assertEqual(Credentials.displayCredential(), Credentials.credentials)
if __name__ == '__main__':
    unittest.main()

