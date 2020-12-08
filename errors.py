#!/usr/bin/env python3.9
assistant_name= "[PANDA]"
def incorrectChoiceError():
    error = f"""
    {assistant_name} 
            You entered wrong choice; 
            Please enter correct choice.
            """
    return print(error)
def UnknowError():
    error = f"""
    {assistant_name} 
            Hey there, sorry to say but unknown error
            is occured. And we apolozied for our 
            inconvenience, we will solve your issue 
            as soon possiable as. 
            """
    return print(error)

def offlineError():
    error = f """
    {assistant_name}
            Hey there, please check your internet connecation 
            
            How to solve :) 
                1) Turn on your wifi or internet connection 
                2) Replug the ethernet cable
                """
    return print(error)

offlineError()