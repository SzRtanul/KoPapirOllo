import tkinter as tk
import time

def open_file(name: str):
    print(name)

if __name__ == '__main__':
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    window.update()

    window2 = tk.Tk()

    for i in range(6):
        window2.columnconfigure(i, weight=1, minsize=75)
        window2.rowconfigure(i, weight=1, minsize=50)
        for j in range(6):
            frame = tk.Frame(
                master=window2,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()

    window2.update()

    window3 = tk.Tk()
    greeting3 = tk.Label(text="What is your name? ")
    greeting3.pack()
    entry=tk.Entry()
    entry.pack()


    La_name=(tk.Label(text=f"{entry.get()}"))
    La_name.pack()

    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(frm_buttons, text="Open", command=lambda: open_file(entry.get()))
    btn_open.pack()
    frm_buttons.pack()
    window3.mainloop(0)