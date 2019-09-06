import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user=User("Emerance Ny","Female","emy","123")

    def test_init(self):
        self.assertEqual(self.new_user.name,"Emerance Ny")
        self.assertEqual(self.new_user.gender,"Female")
        self.assertEqual(self.new_user.username,"emy")
        self.assertEqual(self.new_user.password,"123")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)

    def tearDown(self):
        User.users=[]

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user=User("Gloria","Female","gogo","345")
        test_user.save_user()
        self.assertEqual(len(User.users),2)

if __name__=='__main__':
    unittest.main()
