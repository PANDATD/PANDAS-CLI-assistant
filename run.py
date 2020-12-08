#!/usr/bin/env python3.9 
######## IMPOTED ALL LIBERRIES ######### 
from login import Login 
from Assistant import  welcome , get_choice ,clear

import time as t 
# START MAIN 

if __name__ == '__main__':
    
    clear() 
    welcome()
    Login()
    t.sleep(3)
    print('clearing  screen ... !')
    t.sleep(2)
    clear()
    get_choice()
#  END OF MAIN 

#-------------------------------------------------------------------------------------------------------------------------