import tkinter as tk
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""

def goal():
    global tori
    tori = tk.PhotoImage(file = "fig/6.png")
    canv.create_image(cx, cy, image=torig)
    root.mainloop

def main_proc():
    global mx, my
    global cx, cy

    if key == "Up":
            my -= 1
    if key == "Down":
            my += 1
    if key == "Left":
            mx -= 1
    if key == "Right":
            mx += 1
    if maze_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
                my += 1
        if key == "Down":
                my -= 1
        if key == "Left":
                mx += 1
        if key == "Right":
                mx -= 1

    canv.coords("tori", cx, cy)
    if cx == 1450:
        if cy == 850:
                goal()
    root.after(100, main_proc)





def count_down():
    global tmr
    tmr -= 1
    label["text"] = tmr
    root.after(1000, count_down)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv =  tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_list = mm.make_maze(15, 9)
    print(maze_list)
    mm.show_maze(canv, maze_list)
    canv.create_rectangle(100, 100, 200, 200, fill="blue")
    canv.create_rectangle(1300, 700, 1400, 800, fill="red")

    tori = tk.PhotoImage(file = "fig/0.png")
    
    mx, my = 1, 1
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori")

    key = ""

    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()