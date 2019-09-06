import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential=Credential("facebook","Emerance","123")

    def test_init(self):
        self.assertEqual(self.new_credential.accountName,("facebook"))
        self.assertEqual(self.new_credential.username,"Emerance")
        self.assertEqual(self.new_credential.password,"123")

    def test_save_credential(self):
        self.new_credential.save_credential
        # self.assertEqual(len(Credential.credentials_list),1)

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential=Credential("facebook","Emerance","123")
        test_credential.save_credential

        self.new_credential.delete_credential()
        # self.assertEqual(len(Credential.credentials_list),1)

    def test_findCredential(self):
        self.new_credential.save_credential()
        test_credential=Credential("instagram","Emile","123")
        test_credential.save_credential()

        findCredential=Credential.find_by_accountname("instagram")
        self.assertEqual(findCredential.password,test_credential.password)

    def test_displayCredentials(self):
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

if __name__=='__main__':
    unittest.main()

