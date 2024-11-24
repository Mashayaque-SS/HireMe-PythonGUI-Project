import tkinter as tk

# create the first window
window1 = tk.Tk()
window1.title("First Window")

# create a button in the first window that opens the second window
def open_window2():
    window2 = tk.Toplevel()
    window2.title("Second Window")
    
button = tk.Button(window1, text="Open Second Window", command=open_window2)
button.pack()

# show the first window and start the event loop
window1.mainloop()
