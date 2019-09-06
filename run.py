#!/usr/bin/env python3.6

from user import User
from credential import Credential

def create_users(username,password):
    new_user= User(username,password)
    return new_user

def save_users(user):
    user.save_user()

def delete_users(user):
    user.delete_user()

def find_users(username):
    return User.find_by_username(username)

def display_users():
    return User.display_users()

def create_crededentials(accountName,username,password):
    new_credential=Credential(accountName,username,password)
    return new_credential

def save_credentials(credential):
    credential.save_credential()

def delete_credentials(credential):
    credential.delete_credential()

def find_credentials(accountName):
    return Credential.find_by_accountname(accountName)

def display_credentials():
    return Credential.display_credentials()

def main():
    
    print("WELCOME TO OUR PASSWORD LOCKER APP")
    print("***********************************")
    print("\n")

    while True:
        # print("Do you have have an account ? (y/n)")
        # choice=input()
        # if choice =="n":
           print("CREATE ACCOUNT")
           print("**************")
           print("\n")
           print("Please Enter your username: ")
           cUserName=input() 
           print("Please enter your password")
           cPassword=input()
           save_users(create_users(cUserName,cPassword))
           
           print("\n")
           print(f"User {cUserName} created successfully !!")
           print("\n")
           
           print("ENTER YOUR LOGIN CREDENTIALS")
           print("****************************")
           print("Enter username: ")
           lUserName=input()
           print("Enter Password: ")
           lPassword=input()
           
           if cUserName==lUserName :
              print("Please Enter :: a:Create a new credential, b:display credentials, c:find a credential, d -exit ")
              number=input()
              if number == 'a':
                 print("NEW CREDENTIAL")
                 print("Account Name :")
                 accountName=input()
                 print("Account username: ")
                 username=input()
                 print("Account Password: ")
                 password=input()

                 save_credentials(create_crededentials(accountName,username,password))
                 print("\n")
                 print(f"****Credential {accountName} is created****")
                 print("\n")

              elif number == 'b':
                 if display_credentials():
                    print("Here is all your credentials")
                    print("\n")
                                        
                    for credential in display_credentials():
                        print(f"Account Name : {accountName}")
                        print(f"Account username : {username}")
                        print(f"Account password : {password}")
                    print("\n")  
                 else:
                      print('\n')
                      print("You dont seem to have any credentials saved yet")
                      print('\n')

              elif number == 'c' :
                    print("Enter the account name you want to search for :")
                    search_name=input()
                    if  find_credentials(search_name):
                        search = find_credentials(search_name)
                        print(f"Account Name : {search.accountName}")
                        print(f"Account username : {search.username}")
                        print(f"Account password : {search.password}")

                    else:
                        print("That credential does not exist")

              elif number == 'd' :
                    print(f"Thank you {cUserName} for using our app, Bye...")
                    break
              else:
                    print("I really didn't get that. Please use the letters")
           else:
                print("Invalid login credentials...")
        
        





if __name__ == '__main__':

    main()