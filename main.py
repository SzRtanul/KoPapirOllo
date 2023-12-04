import tkinter as tk
import time

if __name__ == '__main__':
    # greeting = tk.Label(text="Hello, Tkinter")
    #window = tk.Tk()
    #greeting = tk.Label(text="Hello, Tkinter")
    #greeting.pack()
    #window.mainloop()

    window = tk.Tk()

    for i in range(6):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(6):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,


            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()

    window.mainloop()