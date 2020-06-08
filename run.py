######## IMPOTED ALL LIBERRIES ######### 

import webbrowser as wb
import os
import sys 
import smtplib as s 
import wikipedia as wk
import requests
from datetime import datetime 
from login import Login 
import getpass as gp 
import time as t
from Assistant import welcome ,wiki ,search ,search,show_choice ,dinfo,get_choice

#-------------------------------------------------------------------------------------------------------------------------

# START MAIN 

if __name__ == '__main__':
    
    Login()
    welcome()
    get_choice()

#  END OF MAIN 

#-------------------------------------------------------------------------------------------------------------------------