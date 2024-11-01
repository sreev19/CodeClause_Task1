import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2E2E2E")  # Dark background for a modern look
root.resizable(False, False)   # Fixed window size

# Entry field for displaying expressions and results
entry = tk.Entry(root, width=20, font=("Arial", 24, "bold"), borderwidth=2, relief="flat", justify="right", bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), ipady=10)

# Button layout for the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

# Styles for button colors
button_bg = "#4E4E4E"
button_fg = "white"
operator_bg = "#FF9500"
equal_bg = "#5A9E6F"
equal_fg = "white"

# Creating buttons and placing them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18, "bold"),
                           bg=equal_bg, fg=equal_fg, activebackground="#76C69D",
                           command=evaluate_expression)
    elif text in ["/", "*", "-", "+"]:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18, "bold"),
                           bg=operator_bg, fg="white", activebackground="#FFB64C",
                           command=lambda val=text: button_click(val))
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18, "bold"),
                           bg=button_bg, fg=button_fg, activebackground="#6D6D6D",
                           command=lambda val=text: button_click(val))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18, "bold"),
                         bg="#FF3B30", fg="white", activebackground="#FF6B6B", command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=15, sticky="nsew")

# Add padding to grid cells to adjust button size
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i-1, weight=1)

root.mainloop()
