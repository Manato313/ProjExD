import imp
import tkinter as tk
import maze_maker as mm #演習8

def key_down(event):
    global key
    key = event.keysym #演習5

def key_up(event):
    global key
    key = "" #演習6

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Right":
        mx += 1
    if key == "Left":
        mx -= 1
    if maze_list[my][mx] == 0:
        cx,cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my -= 20
        if key == "Down":
            my += 20
        if key == "Right":
            mx += 20
        if key == "Left":
            mx -= 20
    canv.coords("tori", cx,cy)
    root.after(100,main_proc)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#演習1

    canv = tk.Canvas(width = 1500,height = 900, bg = "black")#演習2
    canv.pack()

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canv,maze_list)

    tori = tk.PhotoImage(file = "fig/7.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image = tori, tag = "tori")#演習3

    key = ""#演習4

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #演習7
    main_proc()

    root.mainloop()