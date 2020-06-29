
from random import choice#inbuilt function in Python programming language that returns a random item 
import string
class Credential:

    credential_list = []  # Empty credentials list


def __init__(self, account, password, account_password):

      # docstring removed for simplicity

        self.account = account
        self.password = account_password
        self.account_password = account_password
        
##Saving credentials
def save_credential(self):

        '''
        save_credential method saves credentials objects into credential_list
        '''

        Credential.credential_list.append(self) 
        
##Generating password
@classmethod
def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        # Length of the generated password
        size = 12

        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password
##Check credentials exist

# @classmethod
# def credential_exist(cls, account):

        
#         for credential in cls.credential_list:
#             if credential.account == account:
#                 return True
            
#         return False
##Display credentials
# @classmethod
# def display_credential(cls,password):

        # user_credential_list = []

        # for credential in cls.credential_list:
        #     if credential.user_password == password:
        #         user_credential_list.append(credential)

        # return user_credential_list