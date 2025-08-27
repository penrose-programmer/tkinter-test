import tkinter as tk

window = tk.Tk()
window.title("Delta Calc")
window.configure(
    bg="#0A0C0D",
)

title = tk.Label(
    text="Hello, World!",
    font=("Monospace", 48),
    fg="white",
    bg="#0A0C0D"
)

description = tk.Label(
    text="This is a tkinter test!",
    font=("Monospace", 12),
    fg="white",
    bg="#0A0C0D"
)

field = tk.Text(
    bg="#24292e",
    fg="white",
    insertbackground="white",
    highlightthickness="0",
    borderwidth="0",
    width="40",
    height="15",
    padx="10",
    pady="10"
)

button = tk.Button(
    text="Click Me!",
    bg="#5FED83",
    fg="black",
    highlightthickness="0",
    borderwidth="0",
    width="10",
    height="2",
)

title.pack(padx="10", pady="40")
description.pack(padx="10", pady="10")
field.pack(padx="10", pady="10")
button.pack(padx="10", pady="10")

window.mainloop()
