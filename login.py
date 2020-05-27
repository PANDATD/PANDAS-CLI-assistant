import os 
import getpass as gp 

username = 'root'
password = 'toor'

def Login ():
    
    print('Note :Deafult username  is root  \n')

    get_username = input('Enter you user name : ')
    psswd = gp.getpass('Enter your password : ')

    if get_username == username and psswd == password:
        print('login sucessfull ')
    else :
        print("try again ")
        Login()

    
    