import tkinter as tk

def disLabel():
    lbl.configure(text="こんにちわ")

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk. Button(text="PUSH", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
