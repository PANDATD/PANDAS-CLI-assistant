#!/bin/bash 
echo "checking updates if any updates we will update it "
echo "Installing requiered dependancies "
pip3 install -r requirements.txt 
echo "install required depndancies"
clear 
echo "Resolved depndancies"
echo "executing pandas assistant ."
python3 main.py 
