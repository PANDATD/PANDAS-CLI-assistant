import os 
import getpass as gp 
import Account as ac
import time as t
username = ac.name
password = ac.retype_password 

def Login ():
    

    get_username = input('[pandatd] Enter you user name :\n [you] ' )
    psswd = gp.getpass('[pandatd] Enter your password : \n [you] ')

    if get_username == username and psswd == password:
        print('[pandatd] Please wait miniute Valiedating your password with acording to your username \n')
        t.sleep(2)
        print('[pandatd] login sucessfull \n')
    else :
        print("[pandatd] Try again ")
        print('[pandatd] Please wait for 10 second you have enterd wrong password ')
        t.sleep(10)
        get_choice = input("You want to login or exit if login press 'l' ").lower()
        if get_choice == 'l':
            Login()
        else: 
            print('[pandatd] Bye .. ')


    
