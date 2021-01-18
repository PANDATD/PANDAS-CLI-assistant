import webbrowser as wb
import wikipedia as wk 
from os import system,name 
from time import sleep 
import smtplib as s  
import getpass as gp 
import errors as e
import pyfiglet 

assistant_name = "[PANDA]"

def show_choice():
    clear()
    result = pyfiglet.figlet_format("PANDA-CLI-Assistant",font="slant") 
    show_ch =f"""
    -------------------- SERVICES BY PANDA-CLI-Assistant --------------
    {result}
    -By Mr.Tejas Dixit 
    -------------------------------------------------------------------
    NOTE :-  
        1) Enter the service number  you want to execute.
    -------------------------------------------------------------------
    SERVICES :- 
    -------------------------------------------------------------------
        1)Browsing 
        2)Wikipedia 
        3)You-Tube 
        4)Email
        5)Devloper Guide 
        6)Exit from 
    ------------------------------------------------------------------- 
    """        
    print(show_ch)


def get_choice():
    show_choice()
    try:
        choice = input(f"{assistant_name}Enter Your choice :\n")
    except:
        return get_choice()

    if choice == '1':
        return Browsing()
    elif choice == '2':
        return wiki()
    elif choice == '3':
        return youtube()
    elif choice == '4':
        return sendmail()
    elif choice == '5':
        return dinfo()
    else:
       return e.incorrectChoiceError()


def wiki():
    clear()
    try:
        topic = input(f"{assistant_name} Enter Your Topic-Name   To Search :\n\n [You]").lower()
        print(f'{assistant_name} You Enterd this topic : ',topic)
        print('\n')
        print(f"{assistant_name} Releted searches are : \n")
        result = wk.search(topic)

        i = 1
        for results  in result :
            print (i ,' | ',results )
            i = i+1 
        dec = wk.summary(topic)
        print('\n')

        print('\t',dec,' ')
        get_ch = input(f'{assistant_name} Do you want  to save teh output [y | n]\n[you]').lower()
        if get_ch == 'y' :
            getfnm = input(f"{assistant_name}Type name to save the file : \n[you]")
            f = open (getfnm,'w')
            dec = wk.summary(topic)
            f.write(dec)
            f.close()    
    except:
        print
        get = input(f'{assistant_name} Do you want search again if yes press y or press any key :\n[you]')
        if get == 'y':
            return wiki()
    return get_choice ()


def sendmail():
    clear()
    print(f'{assistant_name}Wait for some time ...! ')
    try:
        ob = s.SMTP('smtp.gmail.com',587) 
        mailadd = input(f'{assistant_name}Enter your email\n\n[you]').lower()
        password = gp.getpass(f'{assistant_name} Enter your password \n\n[you]')
       
        try:
            ob.starttls()
            print(f'{assistant_name}Esatbish secure connecation ...') 
            print(f'{assistant_name}Connecation Established !')
            ob.login(mailadd,password)
            print(f'{assistant_name}Trying to login in...')
            print(f'{assistant_name}Login Sucessfully !')
          
            resiver = input(f'{assistant_name} Enter resiver email.\n\n[you]')
            
            subject = input(f'{assistant_name} Enter Subject for email.\n\n[you]')
            
            body = input(f'{assistant_name} Enter Content for email.\n\n[you]')
            
            message = "subject :{}\n\nBody:{}".format(subject,body) 
            print(message)
           
            ob.sendmail(mailadd,resiver,message)
            ob.quit()
            
            print('Email send sucessfully !! ')
            print('Connecation Closed !!')
        except:
            print(f'{assistant_name} ENTER VALID EMAIL AND PASSWORD ')
    except:
        return e.UnknowError() 
        print(f'{assistant_name} PLEASE TRY AGAIN LATER,\
        \n\t AND CHECK INTERNET CONNECATION OR TURN OFF YOUR AEROPLANE MODE') 
        print('')

    return get_choice()


def Browsing():
    choice_list =f"""
    -------------------------------------------------------------------
    NOTE:- Select your search engine :)
    -------------------------------------------------------------------
        1.1)duckduckgo [ Deafult and privecy based ]
        1.2)google [ Recommonded when you want exact result and fast ]
    -------------------------------------------------------------------    
            """
    print(choice_list)
    try:
        choice = input(f"{assistant_name}Enter Your choice :\n")
        if choice == '1.1':
            search1 = input(f'{assistant_name} Enter Text What you Have to Search !\n[you]')
            print('Tab no 1 :', search1)
            wb.open_new_tab('https://www.duckduckgo.com/?q='+search1)
        elif choice == '1.2':
            search1 = input(f'{assistant_name} Enter Text What you Have to Search !\n[you]')
            print('Tab no 1 :', search1)
            wb.open_new_tab('https://www.google.com/search?q='+search1)
        else :
            return e.incorrectChoiceError()        
    except:
        return e.offlineError()
        
    get = input(f'{assistant_name} Do you want search again[Y/n]').lower()
    if get == 'y':
        return Browsing() 
    else:
        return get_choice()


def youtube():
    clear()
    try:
        searchq = input(f'{assistant_name}Enter youtube serach : ')
        t.sleep(1)
        print(f'{assistant_name} Opening Youtube within your search! \n')
        wb.open_new('www.youtube.com/results?search_query='+searchq) 
    except:
        print(f"{assistant_name} Unknow Error or try after some time ok ! ")
    return get_choice()


def dinfo():
    info ="""
    -------------------------------------------------------------------
                    Devloper Info 
    -------------------------------------------------------------------
    Devloper = Mr. Tejas Vinykant Dixit 
    Instagram = https://www.instagram.com/_pandatd 
    GitHub = https://www.github.com/pandatd
    Twitter = https://www.twitter.com/panda__td
    Email = tejasdixit17@gmail.com , pandatd@protonmail.com
    -------------------------------------------------------------------
    WHO IM I :)
            Hey there,
            im highly python and linux enthusiast 
            who really likes to code in python 
     -------------------------------------------------------------------        
    """
    print(info)
    
 
def clear(): 
	if name == 'nt': 
        
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
        
		_ = system('clear') 
