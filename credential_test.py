import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        # Create credential object
        self.new_credential = Credential("Facebook","dela")

    def tearDown(self):
        Credential.credential_list = []
        
    # def test_init(self):
        
    #     self.assertEqual(self.new_credential.account, "Facebook")
    #     self.assertEqual(self.new_credential.password, "dela" )
    

if __name__ == '__main__':
    unittest.main()