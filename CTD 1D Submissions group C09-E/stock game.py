#-------Importing tkinter for GUI-------
from tkinter import *
from tkinter import ttk

#-------Reading news from text file-------
with open('news.txt') as f:
   nstr=f.read()
   nlist=nstr.split("+")

#-------Defining Variables-------
capital = 1000
stk1 = {"name": "Tesla", "quantity": 0, "price": 100}
stk2 = {"name": "Alibaba", "quantity": 0, "price": 100}
stk3 = {"name": "Singapore Airlines", "quantity": 0, "price": 100}
stk4 = {"name": "ExxonMobil", "quantity": 0, "price": 100}
error_msg = ""
storycounter = -1

#-------Defining Functions to be assigned to buttons-------

'''The buy function takes the stock and the stock quantity labels as input parameters.
If the user has less capital than the price of the stock, then the global error_msg variable is
changed accordingly and the error label is updated.
If the user has sufficient capital, the quantity of the stock increases by 1 and the global variable
capital is reduced by the price of the stock. The stock quantity and capital labels are updated and
the error label is cleared.'''

def buy(stk,stkq):
   global capital
   global error_msg
   if capital < stk["price"]: 
      error_msg = "Error: you don't have enough capital"
      errorlbl.config(text=error_msg)
   else: 
      stk["quantity"]+=1
      stkq.config(text=stk["quantity"])
      capital -= stk["price"]
      capitallbl.config(text="Capital: $"+str(capital))
      error_msg = ""
      errorlbl.config(text=error_msg)

'''The sell function takes the stock and the stock quantity labels as input parameters.
If the user does not have any of the specified stock (i.e. its quantity is 0), then the global error_msg
variable is changed accordingly and the error label is updated.
If the user owns the stock, the quantity of the stock is reduced by 1 and the global variable capital is
increased by the price of the stock. The stock quantity and capital labels are updated and the error
label is cleared.'''

def sell(stk,stkq):
   global capital
   global error_msg
   if stk["quantity"]<=0:
      error_msg = "Error: you don't own this stock"
      errorlbl.config(text=error_msg)
   else:
      stk["quantity"]-=1
      stkq.config(text=stk["quantity"])
      capital += stk["price"]
      capitallbl.config(text="Capital: $"+str(capital))
      error_msg = ""
      errorlbl.config(text=error_msg)

'''The next_turn function takes no input parameters. However, it uses the global storycounter variable
to determine what set of stock prices and news should be shown. It then increments the storycounter by 1.
Once the storycounter reaches 4, it updates the text displayed on the button from “next turn” to “end game”.
Once the storycounter reaches 5, it clears the frame and displays some text to indicate to the user that they
have finished the game.'''

def next_turn():
   global storycounter
   global stk1,stk2,stk3,stk4
   storycounter+=1
   if storycounter <4:

      stk1["price"]=data[storycounter][1]
      stk2["price"]=data[storycounter][2]
      stk3["price"]=data[storycounter][3]
      stk4["price"]=data[storycounter][4]

      news.config(text=data[storycounter][0])
      stk1p.config(text="$"+str(stk1["price"]))
      stk2p.config(text="$"+str(stk2["price"]))
      stk3p.config(text="$"+str(stk3["price"]))
      stk4p.config(text="$"+str(stk4["price"]))

      error_msg = ""
      errorlbl.config(text=error_msg)

   elif storycounter==4:

      stk1["price"]=data[storycounter][1]
      stk2["price"]=data[storycounter][2]
      stk3["price"]=data[storycounter][3]
      stk4["price"]=data[storycounter][4]

      news.config(text=data[storycounter][0])
      stk1p.config(text="$"+str(stk1["price"]))
      stk2p.config(text="$"+str(stk2["price"]))
      stk3p.config(text="$"+str(stk3["price"]))
      stk4p.config(text="$"+str(stk4["price"]))
      next.config(text="End Game")

      error_msg = ""
      errorlbl.config(text=error_msg)

   else:
      clearFrame(content)
      endlbl = ttk.Label(content, text="Congratulations, you finished the game with $"+str(capital))
      perflbl = ttk.Label(content, text=check_capital())
      tylbl = ttk.Label(content, text= "Thank you for playing our game!")
      closebtn = ttk.Button(content, text="Close", command=root.destroy)
      endlbl.grid(column=0,row=0,sticky=(N, S, E, W))
      perflbl.grid(column=0,row=1,sticky=(N, S, E, W))
      tylbl.grid(column=0,row=2,sticky=(N, S, E, W))
      closebtn.grid(column=0,row=3,sticky=(N, S, E, W))

'''The check_capital function takes no input parameters. It checks the global capital variable and returns a
message depending on how much capital is left at the end of the game. This message lets the user know how they
have performed. This function is used within the next_turn function
'''

def check_capital():
   if capital>3000:
      return "You did an amazing job, more than tripling your starting capital."
   elif 2000<capital<=3000:
      return "You did a great job, more than doubling your starting capital."
   elif 1000<capital<=2000:
      return "You did a good job, you managed to increase your capital."
   elif capital == 1000:
      return "You managed to maintain your capital."
   else:
      return "Unfortunately, you lost money."

'''The clearFrame function uses a for loop to clear the widgets within a frame. This function is used within the
next_turn function.'''

def clearFrame(frame):
   # destroy all widgets from frame
   for widget in frame.winfo_children():
      widget.destroy()

#-------Stored Text and Data-------
data = [[nlist[1],100,85,95,80],
        [nlist[2],55,90,90,85],
        [nlist[3],150,100,85,80],
        [nlist[4],180,105,50,50],
        [nlist[5],705,110,50,55]]

#-------Creating the initial game window-------
master = Tk()
master.title("Stock Game")
titlelbl =Label(master, text="Welcome to the stock game!")
desclbl =Label(master, text=nlist[6])

closebtn=ttk.Button(master, text="Play", command=master.destroy)
titlelbl.grid(column=0,row=0,sticky=(N, S, E, W))
desclbl.grid(column=0,row=1,sticky=(N, S, E, W))
closebtn.grid(column=0,row=2,sticky=(N, S, E, W))
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=5)
master.rowconfigure(2, weight=1)
master.columnconfigure(0,weight=1)

master.mainloop()

#-------An instance of a Tkinter Window-------
root = Tk()
root.title("Stock Game")

#-------Creating Frames-------
content = ttk.Frame(root, padding=(5,5,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)

#-------Creating Labels-------
news = ttk.Label(content, text=nlist[0])
namelbl = ttk.Label(content, text="Name")
pricelbl = ttk.Label(content, text="Price")
quantlbl = ttk.Label(content, text="Quantity")
choicelbl = ttk.Label(content, text="Choice")
stk1n = ttk.Label(content, text=stk1["name"])
stk2n = ttk.Label(content, text=stk2["name"])
stk3n = ttk.Label(content, text=stk3["name"])
stk4n = ttk.Label(content, text=stk4["name"])
stk1p = ttk.Label(content, text="$"+str(stk1["price"]))
stk2p = ttk.Label(content, text="$"+str(stk2["price"]))
stk3p = ttk.Label(content, text="$"+str(stk3["price"]))
stk4p = ttk.Label(content, text="$"+str(stk4["price"]))
stk1q = ttk.Label(content, text=stk1["quantity"])
stk2q = ttk.Label(content, text=stk2["quantity"])
stk3q = ttk.Label(content, text=stk3["quantity"])
stk4q = ttk.Label(content, text=stk4["quantity"])
errorlbl = ttk.Label(content, text=error_msg)
capitallbl= ttk.Label(content, text="Capital: $"+str(capital))

#-------Creating Buttons-------
buy1 = ttk.Button(content, text="Buy", command=lambda: buy(stk1,stk1q))
buy2 = ttk.Button(content, text="Buy", command=lambda: buy(stk2,stk2q))
buy3 = ttk.Button(content, text="Buy", command=lambda: buy(stk3,stk3q))
buy4 = ttk.Button(content, text="Buy", command=lambda: buy(stk4,stk4q))

sell1 = ttk.Button(content, text="Sell", command=lambda: sell(stk1,stk1q))
sell2 = ttk.Button(content, text="Sell", command=lambda: sell(stk2,stk2q))
sell3 = ttk.Button(content, text="Sell", command=lambda: sell(stk3,stk3q))
sell4 = ttk.Button(content, text="Sell", command=lambda: sell(stk4,stk4q))

next= ttk.Button(content, text="Next Turn", command=lambda: next_turn())

#-------Establishing the Grid for the buttons and labels-------
content.grid(column=0, row=0, sticky=(N, S, E, W))

#-------Placing the News and a Frame around it-------
frame.grid(column=0, row=0, columnspan=5, rowspan=1, sticky=(N, S, E, W))
news.grid(column=0, row=0, columnspan=5, rowspan =1, sticky=(N, S, E, W), pady=20, padx=20)

#-------Creating the table for the stocks-------
namelbl.grid(column=0,row=1,sticky=(N, S, E, W))
stk1n.grid(column=0,row=2,sticky=(N, S, E, W))
stk2n.grid(column=0,row=3,sticky=(N, S, E, W))
stk3n.grid(column=0,row=4,sticky=(N, S, E, W))
stk4n.grid(column=0,row=5,sticky=(N, S, E, W))

pricelbl.grid(column=1,row=1,sticky=(N, S, E, W))
stk1p.grid(column=1,row=2,sticky=(N, S, E, W))
stk2p.grid(column=1,row=3,sticky=(N, S, E, W))
stk3p.grid(column=1,row=4,sticky=(N, S, E, W))
stk4p.grid(column=1,row=5,sticky=(N, S, E, W))

quantlbl.grid(column=2,row=1,sticky=(N, S, E, W))
stk1q.grid(column=2,row=2,sticky=(N, S, E, W))
stk2q.grid(column=2,row=3,sticky=(N, S, E, W))
stk3q.grid(column=2,row=4,sticky=(N, S, E, W))
stk4q.grid(column=2,row=5,sticky=(N, S, E, W))

choicelbl.grid(column=3,row=1,columnspan=2,sticky=(N, S, E, W))

buy1.grid(column=3,row=2,sticky=(N, S, E, W))
buy2.grid(column=3,row=3,sticky=(N, S, E, W))
buy3.grid(column=3,row=4,sticky=(N, S, E, W))
buy4.grid(column=3,row=5,sticky=(N, S, E, W))

sell1.grid(column=4,row=2,sticky=(N, S, E, W))
sell2.grid(column=4,row=3,sticky=(N, S, E, W))
sell3.grid(column=4,row=4,sticky=(N, S, E, W))
sell4.grid(column=4,row=5,sticky=(N, S, E, W))

#-------Placing the labels/button at the bottom-------
errorlbl.grid(column=0,row=6,columnspan=3,sticky=(N, S, E, W))
capitallbl.grid(column=3,row=6,columnspan=1,sticky=(N, S, E, W))
next.grid(column=4,row=6,columnspan=1,sticky=(N, S, E, W))

#-------Configuring the columns and rows to scale-------
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.rowconfigure(0, weight=6)
for i in range(5):
   content.columnconfigure(i, weight=1)
for i in range(1,6):
   content.rowconfigure(i, weight=1)

#-------Running the window-------
root.mainloop()