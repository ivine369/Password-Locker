import unittest # Importing the unittest module
import pyperclip
from user import User # Importing the user class

class TestUser(unittest.TestCase):
##Check if users are instatianted correctly
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Keith","Sam","Stacey","Brendah") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Brendah")
        self.assertEqual(self.new_user.last_name,"Stacey")
        self.assertEqual(self.new_user.username,"Sam")
        self.assertEqual(self.new_user.password,"Keith")
##Test for saving users
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
##Test to save multiple users
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
##TearDown Method
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
            
##Delete users
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Keith","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
##Finding user
def test_find_user_by_name(self):

        self.new_user.save_user()
        test_user = User("Test","user","Keith","test@user.com") # new user
        test_user.save_user()
        
        found_user = User.find_by_name("Keith")

        self.assertEqual(found_user.password,test_user.password)
        
##Check if contact exists
def test_user_exists(self):


        self.new_user.save_user()
        test_user = User("Test","user","Keith","test@user.com") # new user
        test_user.save_user()

        user_exists = User.user_exist("Keith")

        self.assertTrue(user_exists)
        
##Display users
def test_display_all_users(self):

        self.assertEqual(User.display_users(),User.user_list)
        
##Copy and Paste mechanisms
def test_copy_password(self):

        self.new_user.save_user()
        User.copy_password("Keith")

        self.assertEqual(self.new_user.password,pyperclip.paste())
        
##Login test
# def test_log_in(self):
#         '''
#         Test case to test if a user can log into their credentials
#         '''

#         # Save the new user
#         self.new_user.save_user()

#         test_user = User("Manu","Larry")

#         test_user.save_user()

#         found_user = User.log_in("Manu", "Larry")

#         self.assertEqual( found_user,  User.user_list ) 
        
if __name__ == '__main__':
    unittest.main()