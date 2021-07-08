# CALCULATOR GUI grid

import calclogic as logic
from tkinter import *

txt_field.grid(row=0, column=0, columnspan=4, ipadx=12, ipady=22, pady=17, padx=0)


button7.grid(row=1, column=0, sticky='ew')
button8.grid(row=1, column=1, sticky='ew')
button9.grid(row=1, column=2, sticky='ew')
divide.grid(row=1, column=3, sticky='ew')


button4.grid(row=2, column=0, sticky='ew')
button5.grid(row=2, column=1, sticky='ew')
button6.grid(row=2, column=2, sticky='ew')
multiply.grid(row=2, column=3, sticky='ew')


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
