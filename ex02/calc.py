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

def click_ac(event):        #オールクリア
    entry.delete(0, tk.END)

def click_dl(event):        #1文字消去
    deltxt = entry.get()
    preend = len(deltxt)-1
    entry.delete(preend, tk.END)

def click_fac(event):       #階乗計算
    num = int(entry.get())
    val = 1
    for i in range(num, 1, -1): 
        val *= i
    entry.delete(0, tk.END)
    entry.insert(tk.END, val)

def click_sigma(event):       #総和計算
    num = int(entry.get())
    val = 1
    for i in range(num, 1, -1): 
        val += i
    entry.delete(0, tk.END)
    entry.insert(tk.END, val)

    

root = tk.Tk()
root.title("電卓")
root.geometry("420x700")

entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)


btnac = tk.Button(root, text="AC", font=("", 30), width=4, height=2)
btnac.grid(row=1, column=0)
btnac.bind("<1>", click_ac)


btndl = tk.Button(root, text="←", font=("", 30), width=4, height=2)
btndl.grid(row=1, column=1)
btndl.bind("<1>", click_dl)


btnfac = tk.Button(root, text="!", font=("", 30), width=4, height=2)
btnfac.grid(row=1, column=2)
btnfac.bind("<1>", click_fac)


btnsigma = tk.Button(root, text="Σ", font=("", 30), width=4, height=2)
btnsigma.grid(row=1, column=3)
btnsigma.bind("<1>", click_sigma)


r, c = 2, 0
numbers = list(range(9,-1,-1))
for i , num in enumerate(numbers,1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width =4, height=2)
    btn.grid(row=r, column=c)
    btn.bind("<1>", button_click)
    c+=1
    if i%3 ==0:
        r+=1
        c = 0


btnp = tk.Button(root, text="+", font=("Times New Roman", 30), width=9, height=2)
btnp.grid(row=5, column=1, columnspan=2)
btnp.bind("<1>", button_click)

ro = 2
operators = ["-","*","/"]
for i , num in enumerate(operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width =4, height=2)
    btn.grid(row=ro, column=3)
    btn.bind("<1>", button_click)
    ro+=1
    


btne = tk.Button(root, text="=", font=("Times New Roman", 30), width=4, height=2)
btne.grid(row=5, column=3)
btne.bind("<1>", click_equal)
#btne.bind("<Key-Return>", click_equal)

root.mainloop()