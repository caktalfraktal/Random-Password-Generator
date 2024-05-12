import tkinter as tk
import secrets
import string

def generate_password():
    try:
        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12))
        password_entry.delete(0, tk.END)  # Clear the entry field
        password_entry.insert(0, password)  # Insert the new password
    finally:
        password = ' ' * len(password) # Overwrite the password variable before exiting

# Create the main window
root = (tk.Tk)()
root.title("")
root.geometry("175x75")  # Set the window size to pixels

# Create an entry field to display the generated password
password_entry = tk.Entry(root, width=20, justify=tk.CENTER)
password_entry.pack(pady=10)

# Create a button to generate the password
button = tk.Button(root, text="Generate Password", command=generate_password)
button.pack()

# Start the main loop
root.mainloop()