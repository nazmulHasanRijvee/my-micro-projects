import qrcode  # imports qrcode library
import tkinter as tk  # imports tkinter as Tk()
from tkinter import filedialog  # imports filedialog submodule for file saving
import os  # imports system
from PIL import ImageTk  # Pillow library allows tkinter to display png and jgp files

# Declaring a variable to store the qr code image and use it in multiple functions
qr_img = None


# This Function is responsible to take the input convert it to qr code show it in the window
def get_qr_code():
    data_var = data.get().strip()

    if data_var == "":
        lbl_data.config(text="⚠ Please fill all fields", fg="red")
        return

    # Used global keyword to use the global variable qr_image locally in a function
    global qr_img
    qr_img = qrcode.make(data_var)
    # Calls the show_qr function
    show_qr()
    lbl_data.config(text="✅ QR code generated successfully", fg="green")
    etr_data.delete(0, tk.END)  # clears the entry field after generating qr code


# This function creates a new window and displays the qr code image
def show_qr():
    """Create a new window and display the QR code"""
    global qr_img

    # Creating a new window to display the qr code
    top = tk.Toplevel(master=window)
    top.title("Your QR Code")
    top.geometry("300x300")
    top.resizable(False, False)
    # converts PIL image to Tkinter Image
    qr_tk: ImageTk.PhotoImage = ImageTk.PhotoImage(qr_img)
    # noinspection PyTypeChecker
    label = tk.Label(top, image=qr_tk)
    label.image = qr_tk  # keep a reference!
    label.pack(padx=20, pady=20)


# This function saves the generated qr code image to the user specified location
def save_code():
    global qr_img

    if qr_img is None:
        # config updates the label with the error msg in the run time also changes foreground color
        lbl_save.config(text="⚠ Please generate QR code first", fg="red")
        return

    save_data = name_to_save.get()

    if not save_data:
        lbl_save.config(text="⚠ Please fill all fields", fg="red")
        return

    save_dir = filedialog.askdirectory(title="Select Save Location")

    if save_dir:
        # Saves the file in the user specified directory with .png extension
        filepath = os.path.join(save_dir, f"{save_data}.png")
        qr_img.save(filepath)
        lbl_save.config(text=f"✅ Saved at {filepath}", fg="green")


# Creating root or base window
window = tk.Tk()
window.geometry("600x400")
window.title("QR Code Generator")
window.resizable(False, False)


# Variables to store user input
data = tk.StringVar()  # Stores String value
name_to_save = tk.StringVar()


# label widget to show field name and entry widget for file name input
lbl_save = tk.Label(master=window, text="SAVE_AS")
lbl_save.place(x=160, y=100)
etr_save = tk.Entry(
    master=window, textvariable=name_to_save, width=25, font=("Arial", 15)
)
etr_save.place(x=160, y=125)


# label widget to show field name and entry widget for data input
lbl_data = tk.Label(master=window, text="INSIDE QRCODE")
lbl_data.place(x=160, y=155)
etr_data = tk.Entry(master=window, textvariable=data, width=25, font=("Arial", 15))
etr_data.place(x=160, y=175)


# Button to generate QR code
btn_code = tk.Button(
    master=window, text="Get Code", command=get_qr_code, width=30, height=2, bg="grey"
)
btn_code.place(x=192, y=220)


# Button to save generated QR code
btn_save = tk.Button(
    master=window, text="Save as", command=save_code, width=30, height=2, bg="grey"
)
btn_save.place(x=192, y=260)


# .mainloop() runs the gui
window.mainloop()
