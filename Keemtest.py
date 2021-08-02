import unittest
from KeemTest import Credentials
from KeemTest import User

class Testuser(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.user = User("Keem", "1234") 
    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        self.assertEqual(self.user.user_name, "Keem")
        self.assertEqual(self.user.password, "1234")
    def tearDown(self):
        """[summary]
        """        '''
        method to clean up after each test
        '''
        User.userList = []
    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Keem", "1234")  
        test_user.saveUser()
        self.assertEqual(len(User.userList), 2)
if __name__ == '__main__':
    unittest.main()