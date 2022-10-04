import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    txt = button["text"]
    tkm.showinfo("", f"{txt}のボタンがクリックされました")

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

r, c = 0, 0

for i , num in enumerate(range(9, -1, -1),1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width =4, height=2)
    btn.grid(row=r, column=c)
    btn.bind("<1>", button_click)

    c+=1
    if i%3 ==0:
        r+=1
        c = 0



root.mainloop()