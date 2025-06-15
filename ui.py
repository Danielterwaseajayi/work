import tkinter as tk
from tkinter import ttk, messagebox
from bank import create_account, deposit, withdraw

def build_ui():
    root = tk.Tk()
    root.title("Offline Banking App")
    root.geometry("600x400")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # --- Create Account Tab ---
    create_frame = ttk.Frame(notebook)
    notebook.add(create_frame, text='Create Account')

    tk.Label(create_frame, text="Name:").pack(pady=5)
    name_entry = tk.Entry(create_frame)
    name_entry.pack(pady=5)

    tk.Label(create_frame, text="Account Type:").pack(pady=5)
    acc_type = ttk.Combobox(create_frame, values=["savings", "current"])
    acc_type.pack(pady=5)

    def create_acc():
        try:
            name = name_entry.get()
            a_type = acc_type.get()
            create_account(name, a_type)
            messagebox.showinfo("Success", f"{a_type} account created for {name}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(create_frame, text="Create Account", command=create_acc).pack(pady=10)

    # --- Deposit Tab ---
    deposit_frame = ttk.Frame(notebook)
    notebook.add(deposit_frame, text='Deposit')

    tk.Label(deposit_frame, text="Account ID:").pack(pady=5)
    dep_acc_id = tk.Entry(deposit_frame)
    dep_acc_id.pack(pady=5)

    tk.Label(deposit_frame, text="Amount:").pack(pady=5)
    dep_amt = tk.Entry(deposit_frame)
    dep_amt.pack(pady=5)

    def make_deposit():
        try:
            deposit(int(dep_acc_id.get()), float(dep_amt.get()))
            messagebox.showinfo("Success", "Deposit successful.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(deposit_frame, text="Deposit", command=make_deposit).pack(pady=10)

    # --- Withdraw Tab ---
    withdraw_frame = ttk.Frame(notebook)
    notebook.add(withdraw_frame, text='Withdraw')

    tk.Label(withdraw_frame, text="Account ID:").pack(pady=5)
    wdr_acc_id = tk.Entry(withdraw_frame)
    wdr_acc_id.pack(pady=5)

    tk.Label(withdraw_frame, text="Amount:").pack(pady=5)
    wdr_amt = tk.Entry(withdraw_frame)
    wdr_amt.pack(pady=5)

    def make_withdrawal():
        try:
            withdraw(int(wdr_acc_id.get()), float(wdr_amt.get()))
            messagebox.showinfo("Success", "Withdrawal successful.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(withdraw_frame, text="Withdraw", command=make_withdrawal).pack(pady=10)

    root.mainloop()
