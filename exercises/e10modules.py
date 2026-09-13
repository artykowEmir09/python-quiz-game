import tkinter as tk

# Main window
window = tk.Tk()
window.title("For Nowca ❤️")
window.geometry("500x350")
window.resizable(False, False)

# Background
window.configure(bg="#ffe6f0")

# Title
title = tk.Label(
    window,
    text="❤️ This is for you my Prenses👸->🌻 ❤️ ",
    font=("Arial", 24, "bold"),
    bg="#ffe6f0",
    fg="#d6336c"
)
title.pack(pady=30)

# Main message
message = tk.Label(
    window,
    text="You are so beautiful, Nowca\n\nYou are Emir's N vitamin 💊❤️",
    font=("Arial", 18, "bold"),
    bg="#ffe6f0",
    fg="#333333",
    justify="center"
)
message.pack(pady=20)

# Button
def show_message():
    result.config(text="I hope you always smile, Nowca ❤️")

button = tk.Button(
    window,
    text="Click Me ❤️",
    font=("Arial", 13, "bold"),
    bg="#ff6699",
    fg="white",
    padx=20,
    pady=10,
    command=show_message
)
button.pack(pady=10)

# Result
result = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#ffe6f0",
    fg="#d6336c"
)
result.pack(pady=10)

# Run GUI
window.mainloop()