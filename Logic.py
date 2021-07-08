# CALCULATOR LOGIC
from tkinter import *

values = ''
equation = ''

def press(num): 

    global values 

    values = values + str(num)
    equation.set(values)  


def equal(): 

    try: 
        global values 

        total = str(eval(values)) 
        equation.set(total) 
        values = '' 

    except:
        equation.set(values) 
        values = '' 
