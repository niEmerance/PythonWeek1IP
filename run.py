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

