import webbrowser as wb
import os
import sys 
import smtplib as s 
import subprocess as sub
import wikipedia as wk
import requests
from datetime import datetime 

   
def dinfo():
    Devloper = 'Mr. Tejas Vinykant Dixit '
    Instagram = 'https://www.instagram.com/_pandatd '
    GitHub = 'https://www.github.com/pandatd'
    Twitter = 'https://www.twitter.com/panda__td'
    Email = 'tejasdixit17@gmail.com , pandatd@protonmail.com'
    print('----'*27)
    print ('This app is Devloped by',Devloper,'\n\
    \t\tFolllow us on \n\
    \nInstagram:',Instagram,'\nGitHub:',GitHub,'\nTwitter:',Twitter,'\nEmail',Email)
    print('----'*27)
    return get_choice()

def sendmail():
    try:
        ob = s.SMTP('smtp.gmail.com',587)
        mailadd = input('[pandatd]Enter your email\n[you]')
        password = input('[pandatd] Enter your password \n[you]')
        try:
            ob.starttls()
            print('Esatbish secure connecation ...') 
            print('Connecation Established !')
            ob.login(mailadd,password)
            print('Trying to login in...')
            print('Login Sucessfully !')
            print('----'*27) 
            resiver = input('[pandatd] Enter risiver email.\n[you]')
            print('----'*27) 
            subject = input('[pandatd] Enter Subject for email.\n[you]')
            print('----'*27) 
            body = input('[pandatd] Enter Content for email.\n[you]')
            print('----'*27) 
            message = "subject :{}\n\nBody:{}".format(subject,body)
            print(message)
            print('----'*27) 
            ob.sendmail(mailadd,resiver,message)
            ob.quit()
            print('Connecation Closed !!')
        except:
            print('[pandatd]ENTER VALID EMAIL AND PASSWORD ')
    except:
        print('[PANDATD] PLEASE TRY AGAIN LATER,\
        \n\t AND CHECK INTERNET CONNECATION OR TURN OFF YOUR AEROPLANE MODE')    
    return get_choice()

def open_app():
    '''
    appnm = input('Enter app name to open ')
    if appnm == 'spotify':
        sub.Popen('')
    return open_app()
    '''

def wiki():
    try:
        topic = input(" [pandatd] Enter Your Topic-Name   To Search :\n [You]")
        print('----'*10)
        print('\n',wk.summary(topic),'\n')
        print('----'*27)
    except:
        print('[PANDATD]PLEASE MUST WRITE QUERY OR, \n \
        CHECK SPELLING MESTAKES,\n\t PLEASE TRY AGAIN LATER,\
        \n\t AND CHECK INTERNET CONNECATION OR TURN OFF YOUR AEROPLANE MODE ')
        print('----'*27)            
        
        return wiki()
    return get_choice ()
    
def search():
    try:
        print('----'*27)
        search1 = input('[pandatd] Enter Text What you Have to Search !\n[you]')
        print('----'*27)
        search2 = input('[pandatd] Enter Another Text For New Tab  !\n[you]')
        print('----'*27)
        wb.open_new(search1)
        wb.open_new_tab(search2)
    except:
        print('[pandatd] PLEASE CHECK YOUR URL AGAIN,\n \
            CHECK YOUR INTERNET CONNECTION,\n \
            AND TURN OFF YOUR AEROPLANE MODE ')
        return search()
    return get_choice()

def get_choice():
    try:
        choice = int(input(" [pandatd] Enter Your choice : \n [You] "))
    except: 
        print(' PLEASE ENTER RIGHT CHOICE NO !')
        return get_choice()
    if choice == 1:
        return wiki()
    elif choice == 3:
        return sendmail()
    elif choice == 4:
        return search()
    elif choice == 5:
        return dinfo()

def show_choice():
    ct = datetime.now()
    print('')
    print('----'*27) 
    print('\t\t\t>>> Welcome to  pandatd''s Desktop Assistant <<< \n')
    print('Date:',ct.day,'-',ct.month,'-',ct.year,'\t\t\t\t\t\t\t\t\tTime:',ct.hour,'-',ct.minute,'-',ct.second)
    if ct.hour >12:
        print('Good Morning')
    else :
        print('Good Night ')
    print('----'*27) 
    print('\t\t\t>>> Heare are somethings i can serve for you my lord !! \n ')
    print('----'*27)
    print(' \t 1.Search Info from Wikipedia \n \
        2. open App \n \
        3. Send Mail \n \
        4. Search On Webbrowser \n \
        5. Devloper contact  \n ')
    print('----'*27) 

if __name__ == "__main__":
    show_choice()
    get_choice()
