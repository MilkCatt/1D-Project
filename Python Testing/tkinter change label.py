#tested and working on PYTHON 3.8 AND ADDED TO PATH
import tkinter as tk
win = tk.Tk()

def changetext():
	a.config(text="changed text!")
    
a = tk.Label(win, text="hello world")
a.pack()
tk.Button(win, text="Change Label Text", command=changetext).pack()

win.mainloop()