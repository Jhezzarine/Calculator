# CALCULATOR GUI

import calclogic as logic
from tkinter import *

# Root window 
calc = Tk()

# Setting window size
calc.geometry('358x480')

# Setting background color
calc.configure(bg='#B9DDFF')

# Setting window title
calc.title('Calculator') 

# Declaring window is not resizable
calc.resizable(False,False)


# Setting bg color of button frame
button_frame = Frame(calc, bg='#B9DDFF')

# Organizing buttons in their respective assigned fields
button_frame.pack()

# Setting the equation as string
logic.equation = StringVar()
logic.equation.set('0')

# Setting screen field layout and position  
txt_field = Entry(button_frame, textvariable=logic.equation, justify='right', font = ('cambria', 19, 'bold'))

# Setting up the numeric keypad (0-9) with decimal
button1 = Button(button_frame,font= ('times new roman',12),text=' 1 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff', command= lambda: logic.press, height=3, width=8) 
 
button2 = Button(button_frame,font= ('times new roman',12),text=' 2 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(2), height=3, width=8) 
  
button3 = Button(button_frame,font= ('times new roman',12),text=' 3 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(3), height=3, width=8) 

button4 = Button(button_frame,font= ('times new roman',12),text=' 4 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(4), height=3, width=8) 

button5 = Button(button_frame,font= ('times new roman',12),text=' 5 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(5), height=3, width=8) 
  
button6 = Button(button_frame,font= ('times new roman',12),text=' 6 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(6), height=3, width=8) 

button7 = Button(button_frame,font= ('times new roman',12),text=' 7 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(7), height=3, width=8) 
  
button8 = Button(button_frame,font= ('times new roman',12),text=' 8 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(8), height=3, width=8) 
  
button9 = Button(button_frame,font= ('times new roman',12),text=' 9 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(9), height=3, width=8) 

button0 = Button(button_frame,font= ('times new roman',12),text=' 0 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: logic.press(0), height=3, width=8) 

decimal= Button(button_frame,font= ('times new roman',12),text='.',bd=1,relief='ridge',
                fg='black', bg='#e6ecff',command=lambda: logic.press('.'), height=3, width=8) 

#Setting up the operations' buttons
plus = Button(button_frame,font= ('times new roman',12),text=' + ',bd=1,relief='ridge',
              fg='black', bg='#e6ecff',command=lambda: logic.press("+"), height=6, width=8) 

minus = Button(button_frame,font= ('times new roman',12),text=' - ',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command=lambda: logic.press("-"), height=3, width=8) 

multiply = Button(button_frame,font= ('times new roman',12),text=' * ',bd=1,relief='ridge',
                  fg='black', bg='#e6ecff',command=lambda: logic.press("*"), height=3, width=8) 
  
divide = Button(button_frame,font= ('times new roman',12),text=' / ',bd=1,relief='ridge',
                fg='black', bg='#e6ecff',command=lambda: logic.press("/"), height=3, width=8) 

#Setting up the clear button
clear = Button(button_frame,font= ('times new roman',12),text='C',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command= logic.clear, height=3, width=8) 

#Setting up the delete button (clear entry)
ce = Button(button_frame,font= ('times new roman',12),text='CE',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command=lambda:logic.ce, height=3, width=8) 

#Setting up the equal button that will evaluate the whole expression
equal = Button(button_frame,font= ('times new roman',12),text=' = ',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command= logic.equal, height=3) 

# Organizing the buttons through grids
txt_field.grid(row=0, column=0, columnspan=4, ipadx=12, ipady=22, pady=17, padx=0)

# Row 1
button7.grid(row=1, column=0, sticky='ew')
button8.grid(row=1, column=1, sticky='ew')
button9.grid(row=1, column=2, sticky='ew')
divide.grid(row=1, column=3, sticky='ew')

# Row 2
button4.grid(row=2, column=0, sticky='ew')
button5.grid(row=2, column=1, sticky='ew')
button6.grid(row=2, column=2, sticky='ew')
multiply.grid(row=2, column=3, sticky='ew')

# Row 3
button1.grid(row=3, column=0, sticky='ew')
button2.grid(row=3, column=1, sticky='ew')
button3.grid(row=3, column=2, sticky='ew')
minus.grid(row=3, column=3, sticky='ew')

# Row 4 & 5
button0.grid(row=4, column=0, sticky='ew')
ce.grid(row=4, column=1, sticky='ew')
clear.grid(row=4, column=2, sticky='ew')
decimal.grid(row=5, column=0, sticky='ew')
plus.grid(row=4, column=3, rowspan = 2, sticky='nsew')
equal.grid(row=5, column=1, columnspan=2, sticky='ew')

calc.mainloop() 