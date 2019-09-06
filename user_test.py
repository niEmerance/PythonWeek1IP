import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user=User("emy","123")

    def test_init(self):
        self.assertEqual(self.new_user.username,"emy")
        self.assertEqual(self.new_user.password,"123")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)

    def tearDown(self):
        User.users=[]

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user=User("gogo","345")
        test_user.save_user()
        self.assertEqual(len(User.users),2)
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User("emy","123")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users),1)

    def test_findUser(self):
        self.new_user.save_user()
        test_user=User("emy","123")
        test_user.save_user()

        findUser=User.find_by_username("emy")
        self.assertEqual(findUser.password,test_user.password)

    def test_displayUsers(self):
        self.assertEqual(User.display_users(),User.users)

if __name__=='__main__':
    unittest.main()
