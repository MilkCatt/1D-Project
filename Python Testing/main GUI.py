#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from tkinter import *
from  tkinter import ttk


capital = 10000
stk1 = {"name": "Stock 1", "quantity": 0, "price": 100}
stk2 = {"name": "Stock 2", "quantity": 0, "price": 200}
stk3 = {"name": "Stock 3", "quantity": 0, "price": 300}
stk4 = {"name": "Stock 4", "quantity": 0, "price": 400}

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

ws  = Tk()
ws.title('Stonks Game')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=130)
my_game.column("player_name",anchor=CENTER,width=130)
my_game.column("player_Rank",anchor=CENTER,width=130)
my_game.column("player_states",anchor=CENTER,width=130)


my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="Stock Name",anchor=CENTER)
my_game.heading("player_name",text="Price",anchor=CENTER)
my_game.heading("player_Rank",text="Quantity",anchor=CENTER)
my_game.heading("player_states",text="Choice",anchor=CENTER)


my_game.insert(parent='',index='end',iid=0,text='',
values=(stk1["name"],stk1["price"],stk1["quantity"],))
my_game.insert(parent='',index='end',iid=1,text='',
values=(stk2["name"],stk2["price"],stk2["quantity"],))
my_game.insert(parent='',index='end',iid=2,text='',
values=(stk3["name"],stk3["price"],stk3["quantity"]))

my_game.pack()



#Buy Buttons       
# Initialize tkinter window with dimensions 300 x 250             
ws.geometry('300x250')     
  
# Creating a Button
btn = Button(ws, text = 'Buy', command = buy(stk1))
  
# Set the position of button to coordinate (200, 20)
btn.place(x=800, y=20)
btn.config(height=1,width=2)

#Button2
ws.geometry('300x250')     
  
# Creating a Button
btn2 = Button(ws, text = 'Buy', command = buy(stk2))
  
# Set the position of button to coordinate (200, 20)
btn2.place(x=800, y=40)
btn2.config(height=1,width=2)

#Button3
ws.geometry('300x250')     
  
# Creating a Button
btn2 = Button(ws, text = 'Buy', command = buy(stk3))
  
# Set the position of button to coordinate (200, 20)
btn2.place(x=800, y=60)
btn2.config(height=1,width=2)

#Sell button
ws.geometry('300x250')     
  
# Creating a Button
btn2 = Button(ws, text = 'Sell', command = sell(stk1))
  
# Set the position of button to coordinate (200, 20)
btn2.place(x=900, y=60)
btn2.config(height=1,width=2)

#Sell button2
ws.geometry('300x250')     
  
# Creating a Button
btn2 = Button(ws, text = 'Sell', command = sell(stk2))
  
# Set the position of button to coordinate (200, 20)
btn2.place(x=900, y=40)
btn2.config(height=1,width=2)

#Sell button3
ws.geometry('300x250')     
  
# Creating a Button
btn2 = Button(ws, text = 'Sell', command = sell(stk3))
  
# Set the position of button to coordinate (200, 20)
btn2.place(x=900, y=20)
btn2.config(height=1,width=2)


ws.mainloop()


# In[ ]:





# In[ ]:




