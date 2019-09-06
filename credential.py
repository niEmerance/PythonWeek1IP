class Credential :
    credentials_list=[]
    def __init__(self,accountName,username,password):
        self.accountName=accountName
        self.username=username
        self.password=password

    def save_credential(self):
        Credential.credentials_list.append(self)

    def delete_credential(self):
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_accountname(cls,accountName):
        for Credential in cls.credentials_list:
            if Credential.accountName == accountName:
                return Credential

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list