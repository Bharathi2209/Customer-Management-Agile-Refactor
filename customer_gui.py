# customer_gui.py

import tkinter as tk
from tkinter import messagebox, scrolledtext, font
from refactored_customer_module import Customer, CustomerRepository

# Init Repository
repo = CustomerRepository()

# Setup Main Window
window = tk.Tk()
window.title("🧍 Customer Management System")
window.geometry("600x520")
window.configure(bg="#f0f4f8")

# Fonts
title_font = ("Segoe UI", 18, "bold")
label_font = ("Segoe UI", 12)
button_font = ("Segoe UI", 10, "bold")
entry_font = ("Segoe UI", 11)

# --- UI Elements ---

# Title
tk.Label(window, text="Customer Manager", font=title_font, bg="#f0f4f8", fg="#1a73e8").pack(pady=10)

form_frame = tk.Frame(window, bg="#f0f4f8")
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Name:", font=label_font, bg="#f0f4f8").grid(row=0, column=0, sticky="e", padx=10, pady=5)
name_entry = tk.Entry(form_frame, width=35, font=entry_font)
name_entry.grid(row=0, column=1)

# Email
tk.Label(form_frame, text="Email:", font=label_font, bg="#f0f4f8").grid(row=1, column=0, sticky="e", padx=10, pady=5)
email_entry = tk.Entry(form_frame, width=35, font=entry_font)
email_entry.grid(row=1, column=1)

# Phone
tk.Label(form_frame, text="Phone:", font=label_font, bg="#f0f4f8").grid(row=2, column=0, sticky="e", padx=10, pady=5)
phone_entry = tk.Entry(form_frame, width=35, font=entry_font)
phone_entry.grid(row=2, column=1)

# Button Frame
btn_frame = tk.Frame(window, bg="#f0f4f8")
btn_frame.pack(pady=10)

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def add_customer():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    if name and email and phone:
        result = repo.add_customer(Customer(name, email, phone))
        output_box.insert(tk.END, result + "\n")
        clear_fields()
    else:
        messagebox.showwarning("⚠️ Missing Info", "All fields are required!")

def search_customer():
    email = email_entry.get().strip()
    if email:
        customer = repo.get_customer(email)
        if customer:
            output_box.insert(tk.END, f"🔍 Found: {customer}\n")
        else:
            output_box.insert(tk.END, "❌ Customer not found.\n")
    else:
        messagebox.showwarning("⚠️ Input Needed", "Please enter an email.")

def delete_customer():
    email = email_entry.get().strip()
    if email:
        result = repo.delete_customer(email)
        output_box.insert(tk.END, result + "\n")
        clear_fields()
    else:
        messagebox.showwarning("⚠️ Input Needed", "Please enter an email.")

def list_customers():
    customers = repo.list_customers()
    output_box.insert(tk.END, "📋 Customer List:\n")
    for c in customers:
        output_box.insert(tk.END, f" - {c}\n")
    output_box.insert(tk.END, "-"*60 + "\n")

def clear_output():
    output_box.delete("1.0", tk.END)

# Buttons
tk.Button(btn_frame, text="➕ Add", font=button_font, width=12, bg="#4caf50", fg="white", command=add_customer).grid(row=0, column=0, padx=8, pady=5)
tk.Button(btn_frame, text="🔍 Search", font=button_font, width=12, bg="#2196f3", fg="white", command=search_customer).grid(row=0, column=1, padx=8, pady=5)
tk.Button(btn_frame, text="🗑️ Delete", font=button_font, width=12, bg="#f44336", fg="white", command=delete_customer).grid(row=0, column=2, padx=8, pady=5)
tk.Button(btn_frame, text="📋 List All", font=button_font, width=12, bg="#9c27b0", fg="white", command=list_customers).grid(row=1, column=0, padx=8, pady=5)
tk.Button(btn_frame, text="🧹 Clear Output", font=button_font, width=12, command=clear_output).grid(row=1, column=1, padx=8, pady=5)
tk.Button(btn_frame, text="↩️ Clear Fields", font=button_font, width=12, command=clear_fields).grid(row=1, column=2, padx=8, pady=5)

# Output Text Box
output_box = scrolledtext.ScrolledText(window, height=12, width=70, font=("Courier New", 10))
output_box.pack(pady=10)

# Launch GUI
window.mainloop()
