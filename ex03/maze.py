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
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Right":
        cx += 20
    if key == "Left":
        cx -= 20
    canv.coords("tori", cx,cy)
    root.after(100,main_proc)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#演習1

    canv = tk.Canvas(width = 1500,height = 900, bg = "black")#演習2
    canv.pack()

    tori = tk.PhotoImage(file = "fig/7.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image = tori, tag = "tori")#演習3

    key = ""#演習4

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #演習7
    main_proc()
    
    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canv,maze_list)

    root.mainloop()