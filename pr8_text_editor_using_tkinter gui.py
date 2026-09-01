# imports tkinter gui
import tkinter as tk

# importing filedialog submodule for opening a file chooser dialog that opens or saves files.
from tkinter.filedialog import askopenfilename, asksaveasfilename

"""Open a file for editing."""


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


"""Save the current file as a new file."""


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


# .Tk class creates a root window
window = tk.Tk()


# Sets the title of window
window.title("Simple Text Editor")


# configures the row & column when window is expanded
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)


# Creating a frame to contain the buttons
frm_buttons = tk.Frame(window, relief="raised", bd=2)


# Creating the text and button widgets
txt_edit = tk.Text(master=window)
btn_open = tk.Button(master=frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(master=frm_buttons, text="Save As...", command=save_file)


# Creating a 1 row/ 2 column grid
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


# Creating another 2 row/ 1 column grid inside frame and placing button widgets
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


# .mainloop() runs the gui
window.mainloop()
