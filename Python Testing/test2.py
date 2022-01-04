from tkinter import *
from tkinter import ttk

#Defining Variables

capital = 10000
stk1 = {"name": "Stock 1", "quantity": 0, "price": 100}
stk2 = {"name": "Stock 2", "quantity": 0, "price": 200}
stk3 = {"name": "Stock 3", "quantity": 0, "price": 300}
stk4 = {"name": "Stock 4", "quantity": 0, "price": 400}

#Defining Functions

def buy(stk):
   global capital
   if capital < stk["price"]:  
      print("You don't have enough capital")
   else: 
      stk["quantity"]+=1
      capital -= stk["price"]

def sell(stk):
   global capital
   if stk["quantity"]<=0:
      print("You don't own this stock")
   else:
      stk["quantity"]-=1
      capital += stk["price"]

#Creating Table

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()