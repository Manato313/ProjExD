import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END,num)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

root = tk.Tk()
root.geometry("390x500")

entry = tk.Entry(root, width = 14, font = ("", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 5)

r,c = 1, 0
numbers = list(range(9, -1, -1))
operators = ["/", "*", "-", "+"]
for i, num in enumerate(numbers,1):
    if num != 0:
        btn = tk.Button(root, text = f"{num}", font = ("",30), width = 4, height = 2)
        btn.grid(row = r, column = c)
    else:
        btn = tk.Button(root, text = f"{num}", font = ("",30), width = 9, height = 2)
        btn.grid(row = r, column = c, columnspan = 2)
    btn.bind("<1>", click_number)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

for i, operate in enumerate(operators,1):
    op_btn = tk.Button(root, text = f"{operate}",font = ("", 30), width = 4, height = 2)#計算記号追加
    op_btn.grid(row = i, column = 4)
    op_btn.bind("<1>",click_number)

btn = tk.Button(root, text=f"=", font = ("",30), width = 4, height = 2)#イコール追加
btn.bind("<1>", click_equal)
btn.grid(row = r, column = c+1)

root.mainloop()