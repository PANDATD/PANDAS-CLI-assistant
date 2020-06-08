import webbrowser as wb
import os
import sys 
import smtplib as s 
import wikipedia as wk
from datetime import datetime 
from login import Login 
import getpass as gp 
import time as t


###### FUNACATIONS ######

# start of welcome mesage  funcation 
def welcome():
    '''
    welcome message 
    '''
    ct = datetime.now()
    print('')
    print('\t\t\t\t>>> Welcome to  pandatd''s Desktop Assistant <<< \n')
    print('\n')
    print('Date:',ct.day,'-',ct.month,'-',ct.year,'\t\t\t\t\t\t\t\t\tTime:',ct.hour,'-',ct.minute,'-',ct.second)
    print('\n\n')
    print('[pandatd] Heare are some servises, I can provide you !! \n ')
    
# end of welcome mesage Funcation 

#-------------------------------------------------------------------------------------------------------------------------

# START SHOW FUNCATION  

def show_choice():
    
    '''
    List of Services
    ''' 

    print('\n\n')
    print('1. Search Info from Wikipedia.') 
    print('2. Send Mail.')
    print('3. Search On Webbrowser.')
    print('4. Devloper contact.')
    print('5. search on Youtube ')
    print('For exit enter 6 and above no ')
    print('\n\n')

#   END SHOW FUNCATION 


#-------------------------------------------------------------------------------------------------------------------------

# START OF GET CHOICE FUNCATION  

def get_choice():

    show_choice()

    try:
        choice = int(input("[pandatd] Enter Your choice : \n\n"))
    except: 
        print('[pandatd] PLEASE ENTER RIGHT CHOICE NO !')
        return get_choice()
    if choice == 1:
        return wiki()
    elif choice == 2:
        return sendmail()
    elif choice == 3:
        return search()
    elif choice == 4:
        return dinfo()
    elif choice == 5:
        return youtube()

# END OF GET CHOICE FUNCATION 

#-------------------------------------------------------------------------------------------------------------------------

# START WIKIPEDIA FUUNCATION

def wiki():
    
    try:
        topic = input(" [pandatd] Enter Your Topic-Name   To Search :\n\n [You]").lower()
        print(' [pandatd] You Enterd this topic : ',topic)
        print('\n')
        print("[pandatd] Releted searches are : \n")
        result = wk.search(topic)

        i = 1
        for results  in result :
            print (i ,' | ',results )
            i = i+1 
        dec = wk.summary(topic)
        print('\n')

        print('\t',dec,' ')
        get_ch = input('[pandatd] Do you want  to save teh output [y | n]\n[you]').lower()
        if get_ch == 'y' :
            getfnm = input("[pandatd]Type name to save the file : \n[you]")
            f = open (getfnm,'w')
            dec = wk.summary(topic)
            f.write(dec)
            f.close()    
    except:
        print('[PANDATD] PLEASE MUST WRITE QUERY OR, \n \
        CHECK SPELLING MESTAKES,\n\t PLEASE TRY AGAIN LATER,\
        \n\t AND CHECK INTERNET CONNECATION OR TURN OFF YOUR AEROPLANE MODE ')
        print('\n')
        get = input('[pandatd] Do you want search again if yes press y or press any key :\n[you]')
        if get == 'y':
            return wiki()
    return get_choice ()

# END OF WIKIPEDIA FUNCATION

#-------------------------------------------------------------------------------------------------------------------------

# START OF SENDNAIL FUNCATION  

def sendmail():

    try:
        ob = s.SMTP('smtp.gmail.com',587)
        mailadd = input('[pandatd]Enter your email\n\n[you]').lower()
        password = gp.getpass('[pandatd] Enter your password \n\n[you]')
       
        try:
            ob.starttls()
            print('Esatbish secure connecation ...') 
            print('Connecation Established !')
            ob.login(mailadd,password)
            print('Trying to login in...')
            print('Login Sucessfully !')
          
            resiver = input('[pandatd] Enter resiver email.\n\n[you]')
            
            subject = input('[pandatd] Enter Subject for email.\n\n[you]')
            
            body = input('[pandatd] Enter Content for email.\n\n[you]')
            
            message = "subject :{}\n\nBody:{}".format(subject,body) 
            print(message)
           
            ob.sendmail(mailadd,resiver,message)
            ob.quit()
            
            print('Email send sucessfully !! ')
            print('Connecation Closed !!')
        except:
            print('[pandatd] ENTER VALID EMAIL AND PASSWORD ')
    except:
        print('[PANDATD] PLEASE TRY AGAIN LATER,\
        \n\t AND CHECK INTERNET CONNECATION OR TURN OFF YOUR AEROPLANE MODE') 
        print('')

    return get_choice()

# END MAIL FUNCATION

#-------------------------------------------------------------------------------------------------------------------------

# START SEARCH FUNCATION

def search():

    try:
        search1 = input('[pandatd] Enter Text What you Have to Search !\n\n[you]')
        print('\n')
        print('Tab no 1 :', search1)
        t.sleep(0.1)
        wb.open_new('https://www.google.com/search?q='+search1)

        
    except:
        print('[pandatd] PLEASE CHECK YOUR URL AGAIN,\n \
            CHECK YOUR INTERNET CONNECTION,\n \
            AND TURN OFF YOUR AEROPLANE MODE ')
        
        print('\n')

        get = input('[pandatd] Do you want search again if yes press y or press any key ')
        if get == 'y':
            return search()       
    return get_choice()

# END OF SEARCH FUNCATION  

#-------------------------------------------------------------------------------------------------------------------------

# START YOUTUBE FUNCATION 

def youtube():
    try:
        searchq = input('[pandatd]Enter youtube serach : ')
        t.sleep(1)
        print('[pandatd] Opening Youtube within your search! \n')
        wb.open_new('www.youtube.com/results?search_query='+searchq) 
    except:
        print("[pandatd] Unknow Error or try after some time ok ! ")
    return get_choice()

# END OF YOUTUBE FUNCATION 

#-------------------------------------------------------------------------------------------------------------------------
   
# DEVLOPER FINCATION 


def dinfo():
    Devloper = 'Mr. Tejas Vinykant Dixit '
    Instagram = 'https://www.instagram.com/_pandatd '
    GitHub = 'https://www.github.com/pandatd'
    Twitter = 'https://www.twitter.com/panda__td'
    Email = 'tejasdixit17@gmail.com , pandatd@protonmail.com'
    
    print ('This app is Devloped by',Devloper,'\n\
    \t\tFolllow us on \n\
    \nInstagram:',Instagram,'\nGitHub:',GitHub,'\nTwitter:',Twitter,'\nEmail',Email)
    return get_choice()

    
# END OF DEVLOPER FUNCATION

#-------------------------------------------------------------------------------------------------------------------------
