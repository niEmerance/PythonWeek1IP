class User:
    users=[]
    def __init__(self,name,gender,username,password):

        self.name=name
        self.gender=gender
        self.username=username
        self.password=password

    def save_user(self):
        User.users.append(self)