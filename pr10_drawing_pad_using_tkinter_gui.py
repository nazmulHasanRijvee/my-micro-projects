import os  # imports system
import tkinter as tk  # imports tkinter as tk
from tkinter.colorchooser import (
    askcolor,
)  # imports askcolor from colorchooser submodule
from PIL import ImageGrab  # imports ImageGrab library
from tkinter.filedialog import (
    askdirectory,
)  # importing askdirectory from filedialog submodule

# .Tk class creates a root window
window = tk.Tk()
window.title("Simple Drawing Pad")


# Functions for the starting point of drawing
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y  # starting point


# Function for drawing the line
def draw(event):

    global last_x, last_y

    # if there is coordinate value then the code executes
    if last_x and last_y:
        canvas.create_line(
            last_x,
            last_y,
            event.x,
            event.y,
            fill=brush_color,
            width=brush_size.get(),
            capstyle="round",
            smooth=True,
        )
    # Updating the old coordinates with new ones after drawing
    last_x, last_y = event.x, event.y


# Function to erase the canvas
def erase_draw():

    global brush_color
    brush_color = canvas.cget("bg")


# Function to execute when we stop drawing and _ underscore is used to show we don't care about (event) it
def stop_draw(_event):
    # get the last coordinates
    global last_x, last_y
    # Resetting the co-ordinates to null
    last_x, last_y = None, None


# function to pick the color of the brush
def pick_color():
    global brush_color
    res = askcolor(title="Pick brush color")
    # if res variable is not null, and it has a second element which is the hex code it runs
    if res and res[1]:
        # Sets the current brush color to the selected color
        brush_color = res[1]  # hex string like "#ff0000"


# This function is used to clear the canvas completely
def clear_canvas():
    # delete method clears everything
    canvas.delete("all")


# Function to save the drawing as an image
def save_canvas_image():
    # Ask user where to save
    save_dir = askdirectory(title="Select save location")
    if not save_dir:
        return  # User cancelled

    # Update the canvas to ensure latest drawing is rendered
    canvas.update()

    """ --- Screenshot Calibration for Saving the Canvas ---"""
    x = canvas.winfo_rootx() + 15
    y = canvas.winfo_rooty()
    x1 = x + canvas.winfo_width() + 100
    y1 = y + canvas.winfo_height() + 100

    # Construct file path
    filepath = os.path.join(save_dir, "drawing.png")

    # Grab the canvas area from the screen
    ImageGrab.grab(bbox=(x, y, x1, y1)).save(filepath)


# Creating a canvas widget to draw on where parent window is window
canvas = tk.Canvas(master=window, bg="white", width=600, height=400)


# Variables for drawing by default the color is black
brush_color = "black"
# variables track co-ordinates of the mouse
last_x, last_y = None, None
# integer variable for getting the value from slider widget
brush_size = tk.IntVar(value=4)


# Creating a Slider widget to adjust the brush size
size_slider = tk.Scale(
    master=window,
    from_=4,
    to=60,
    orient="horizontal",
    variable=brush_size,
    label="Brush size",
)


# Bind mouse events to draw in the canvas
canvas.bind("<Button-1>", start_draw)  # mouse click
canvas.bind("<B1-Motion>", draw)  # mouse drag
canvas.bind("<ButtonRelease-1>", stop_draw)  # mouse release


# frame widget to contain the buttons
frm = tk.Frame(master=window)
# Button to pick color of the brush
btn_color = tk.Button(master=frm, text="Pick Color", command=pick_color)
# Button to clear canvas
btn_clear = tk.Button(master=frm, text="Clear", command=clear_canvas)
# Button to save canvas as image
btn_save = tk.Button(master=frm, text="Save Drawing", command=save_canvas_image)
# Button to erase
btn_erase = tk.Button(master=frm, text="erase", command=erase_draw)


# Placing the widgets in a 3 row/ 1 column grid
canvas.grid(row=0, column=0)
size_slider.grid(row=1, column=0)
frm.grid(row=2, column=0)


# Creating another 1 row/ 4 column grid inside the frame widget
btn_color.grid(row=0, column=0, padx=5)
btn_erase.grid(row=0, column=1, padx=5)
btn_clear.grid(row=0, column=2, padx=5)
btn_save.grid(row=0, column=3, padx=5)


# .mainloop() runs the gui
window.mainloop()
