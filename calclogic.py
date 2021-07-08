# CALCULATOR LOGIC
from tkinter import *

values = ''
equation = ''

# event function when any button is pressed (except equal and clear button)
def press(num): 

    global values 

    values = values + str(num)
    equation.set(values)  


# event function when equal button is pressed
def equal(): 

    try: 
        global values 

        total = str(eval(values)) 
        equation.set(total) 
        values = '' 

    except:
        equation.set(values) 
        values = '' 


# clear button function 
def clear():
        
    global values
    values = '' 
    equation.set('0')


# delete button function 
def ce():

    global values
    
    new = len(values)
    delete = values[:new-1]
    equation.set(delete)
    values = delete
