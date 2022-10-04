from ast import operator
import numbers
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    button = event.widget
    txt = button["text"]
    #tkm.showinfo("", f"{txt}のボタンがクリックされました")
    entry.insert(tk.END, txt)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)


root = tk.Tk()
root.title("電卓")
root.geometry("300x560")




entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)


r, c = 1, 0
numbers = list(range(9,-1,-1))
operators = ["+"]
for i , num in enumerate(numbers + operators,1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width =4, height=2)
    btn.grid(row=r, column=c)
    btn.bind("<1>", button_click)

    c+=1
    if i%3 ==0:
        r+=1
        c = 0

btne = tk.Button(root, text="=", font=("Times New Roman", 30), width=4, height=2)
btne.grid(row=4, column=2)
btne.bind("<1>", click_equal)



root.mainloop()