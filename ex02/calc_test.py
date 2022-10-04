print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました。ｶﾞｯ‼")
root = tk.Tk()
root.title("ぬるぽ")
root.geometry("500x200")

label = tk.Label(root,
                text = "これらべるだよ",
                font=("Ricty Diminished",20)
                )
label.pack()

button = tk.Button(root, text="NullPointerException")
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(width = 30)
entry.insert(tk.END,"don't")
entry.pack()

root.mainloop()