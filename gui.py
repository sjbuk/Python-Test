import tkinter as tk 
from tkinter import ttk 
# Events
def monthPrint (event):
  print("Clicked")
  print(monthchoosen['value'])


# Creating tkinter window 
window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 
  
# label text for title 
ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Select the Month :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
monthchoosen['textvariable'] = ('01',  
                          '02', 
                          '03', 
                          '04', 
                          '05', 
                          '06', 
                          '07', 
                          '08', 
                          '09', 
                          '10', 
                          '11', 
                          '12') 
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
monthchoosen.bind("<<ComboboxSelected>>",monthPrint)
window.mainloop() 