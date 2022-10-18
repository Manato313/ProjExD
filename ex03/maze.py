from curses import KEY_DOWN
import tkinter as tk

def key_down(event):
    global key
    key = event.keysym #演習5


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

    root.mainloop()