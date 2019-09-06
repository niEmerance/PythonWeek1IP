class User:
    users=[]
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        User.users.append(self)

    def delete_user(self):
        User.users.remove(self)

    @classmethod
    def find_by_username(cls,username):
        for user in cls.users:
            if user.username == username:
                return user
    
    @classmethod
    def display_users(cls):
        return cls.users
        