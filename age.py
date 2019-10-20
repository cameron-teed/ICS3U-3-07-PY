#!/usr/bin/env python3

# Created by: cameron teed 
# Created on: October 2019
# This program tells you if you can date this grandmas daughter 

def main():
    # This program tells you if you can date this grandmas daughter
    
    age = input("Please enter your age: ")
    true = True
    
    while true == True:
    
        try:
        
            age = int(age) 
        
            if age >= 25 and age <= 40:
                print("You can date linda")
        
            elif age < 25:
                print("You are too young to date my Linda")
        
            else: 
                print("Sorry, but you are too old to date Linda")  
                
            break 
        
        except Exception: 
            print("Please enter a nummber")
    


if __name__ == "__main__":
    main()