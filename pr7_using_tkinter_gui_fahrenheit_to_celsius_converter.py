# imports tkinter gui
import tkinter as tk

# .Tk class creates a root window
window = tk.Tk()


# configures the row & column when  its expanded and minimum size is 50 pixel
window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure([0, 1, 2], weight=1, minsize=50)


# Declaring a variable to remember which entry was last typed in
last_edited = None


# This function runs whenever a key is pressed inside an entry widget
def set_last_edited(event):
    # Modifying the variable in this function using global keyword
    global last_edited
    last_edited = event.widget


# Checks the last edited field and converts it.
def convert():
    global last_edited

    if last_edited == entry:  # If Fahrenheit was last edited
        f_val = entry.get()
        if f_val:
            try:
                temp_c = (float(f_val) - 32) * 5 / 9
                entry_c.delete(0, tk.END)
                entry_c.insert(0, f"{temp_c:.2f}")
            except ValueError:
                entry_c.delete(0, tk.END)
                entry_c.insert(0, "Error")

    elif last_edited == entry_c:  # if Celsius was last edited
        c_val = entry_c.get()
        if c_val:
            try:
                temp_f = (float(c_val) * 9 / 5) + 32
                entry.delete(0, tk.END)
                entry.insert(0, f"{temp_f:.2f}")
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "Error")


# Creating a list to store the frames
frmList = []


# Creating a nested loop to create 3 frames and place them in the 1 row / 3 column grid
for i in range(1):
    for j in range(3):
        frame = tk.Frame(master=window, relief="ridge", borderwidth=1)
        frame.grid(row=i, column=j)
        frmList.append(frame)


# Creating an entry widget to take the input from user
entry = tk.Entry(master=frmList[0], width=10, font=("Arial", 25), borderwidth=1)


# Creating a label widget to show the text `F
lbl_f = tk.Label(master=frmList[0], text="`F", height=5, width=3)


# Creating a button widget to tap and start the program
btn_convert = tk.Button(
    master=frmList[1], text="<-->", height=4, width=10, command=convert
)


# Creating another label widget to show the output
entry_c = tk.Entry(master=frmList[2], width=10, font=("Arial", 25), borderwidth=1)


# Creating a label widget to show the text `C
lbl_c = tk.Label(master=frmList[2], text="`C", height=5, width=3)


# Binding the entry widgets with event function to track which one was edited last
entry.bind("<Key>", set_last_edited)
entry_c.bind("<Key>", set_last_edited)
entry.bind("<FocusIn>", set_last_edited)
entry_c.bind("<FocusIn>", set_last_edited)


# Placing the widgets in the frame to show up
entry.pack(side="left")
lbl_f.pack()
btn_convert.pack(padx=5, pady=5)
entry_c.pack(side="left")
lbl_c.pack()


# .mainloop() runs the gui
window.mainloop()
