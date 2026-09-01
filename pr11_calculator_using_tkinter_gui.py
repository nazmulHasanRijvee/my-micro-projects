import tkinter as tk  # imports tkinter as tk


class CalculatorApp:
    # Constructor of the class
    def __init__(self, root):
        # self keyword lets access to root window
        self.root = root
        self.root.title("Colorful Calculator")
        self.root.resizable(True, True)
        self.expression = ""

        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 28),
            bd=10,
            relief="sunken",
            bg="#1e1e1e",
            fg="white",
            justify="right",
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Buttons
        buttons = [
            ("C", 1, 0, "#ff4c4c"),
            ("%", 1, 1, "#ff9800"),
            ("/", 1, 2, "#ff9800"),
            ("*", 1, 3, "#ff9800"),
            ("7", 2, 0, "#4caf50"),
            ("8", 2, 1, "#4caf50"),
            ("9", 2, 2, "#4caf50"),
            ("-", 2, 3, "#ff9800"),
            ("4", 3, 0, "#4caf50"),
            ("5", 3, 1, "#4caf50"),
            ("6", 3, 2, "#4caf50"),
            ("+", 3, 3, "#ff9800"),
            ("1", 4, 0, "#4caf50"),
            ("2", 4, 1, "#4caf50"),
            ("3", 4, 2, "#4caf50"),
            ("=", 4, 3, "#2196f3"),
            ("0", 5, 0, "#4caf50"),
            (".", 5, 2, "#4caf50"),
        ]

        for text, row, col, color in buttons:
            if text == "0":
                self.create_button(text, row, col, color, colspan=2)
            else:
                self.create_button(text, row, col, color)

        # Configure grid weights
        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def create_button(self, text, row, col, color, colspan=1):
        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=5,
            relief="raised",
            command=lambda t=text: self.on_button_click(t),
        )
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_var.set("")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except Exception:
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)


# to have a run the program icon if __name__ == "__main__" is used
if __name__ == "__main__":
    # .Tk class creates a root window
    root = tk.Tk()
    app = CalculatorApp(root)
    # .mainloop() runs the gui
    root.mainloop()
