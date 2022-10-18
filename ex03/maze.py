import tkinter as tk
import maze_maker as mm #演習8

def key_down(event):
    global key
    key = event.keysym #演習5

def key_up(event):
    global key
    key = "" #演習6

def main_proc():
    global jump_stock
    global mx, my
    global cx, cy, tori
    canv.coords("tori", cx,cy)
    if key == "1":
        tori = tk.PhotoImage(file = "fig/1.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "2":
        tori = tk.PhotoImage(file = "fig/2.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "3":
        tori = tk.PhotoImage(file = "fig/3.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "4":
        tori = tk.PhotoImage(file = "fig/4.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "5":
        tori = tk.PhotoImage(file = "fig/5.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "6":
        tori = tk.PhotoImage(file = "fig/6.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "7":
        tori = tk.PhotoImage(file = "fig/7.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "8":
        tori = tk.PhotoImage(file = "fig/8.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "9":
        tori = tk.PhotoImage(file = "fig/9.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "0":
        tori = tk.PhotoImage(file = "fig/0.png")
        bid = canv.create_image(cx, cy, image = tori, tag = "tori")
    if key == "Up":
        my -= 1
        if jump_stock == 1:
            my -= 1
            jump_stock = 0
    if key == "Down":
        my += 1
        if jump_stock == 1:
            my += 1
            jump_stock = 0
    if key == "Right":
        mx += 1
        if jump_stock == 1:
            mx += 1
            jump_stock = 0
    if key == "Left":
        mx -= 1
        if jump_stock == 1:
            mx -= 1
            jump_stock = 0
    if key == "BackSpace":
        mx, my = 1, 1
    if key == "space":
        jump_stock = 1
    if maze_list[my][mx] == 0:
        cx,cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Right":
            mx -= 1
        if key == "Left":
            mx += 1
    
    root.after(100,main_proc)
    

if __name__ == "__main__":
    jump_stock = 0
    root = tk.Tk()
    root.title("迷えるこうかとん")#演習1

    canv = tk.Canvas(width = 1500,height = 900, bg = "black")#演習2
    canv.pack()

    maze_list= mm.make_maze(15, 9)
    mm.show_maze(canv,maze_list)

    tori = tk.PhotoImage(file = "fig/1.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    bid = canv.create_image(cx, cy, image = tori, tag = "tori")#演習3

    key = ""#演習4

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #演習7
    main_proc()

    root.mainloop()