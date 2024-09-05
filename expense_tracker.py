import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def display_exp(expenses):
    print("\nExpense Table:")
    print(f"{'Type' :<15} {'Name':<20} {'Date':<15} {'Amount':<10}")
    print("="*50)


    total = 0

    for expense in expenses:
        print(f"{expense['type']:<15} {expense['name']:<20} {expense['date']:<15} {expense['amount']:<10}")
        total += float(expense['amount'])


    
    print("="*50)
    print(f"Total Expense adds upto: ${total:.2f}\n")


def add_exp_gui():
    def submit_expense():
        expense_type = type_var.get()
        name = name_entry.get()
        date = date_entry.get()
        amount = amount_entry.get()

        # validate date format (DD-MM-YYYY)
        date_pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")
        if not date_pattern.match(date):
            messagebox.showwarning("Invalid date", "Please enter date in DD-MM-YYYY format.")
            return
        
        # validate amount (only numeric)
        if not amount.replace('.', '', 1).isdigit():
            messagebox.showwarning("Invalid Amount", "Please enter a valid amount (numeric value)")
            return

        # Format the amount with "£" symbol
        formatted_amount = f"£{amount}"

        # Add the expense to the table
        tree.insert('', 'end', values=(expense_type, name, date, formatted_amount))

        name_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    
    def delete_expense():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
        else:
            messagebox.showwarning("No Selection", " Please Select an item to delete")


    root = tk.Tk()
    root.title("Expense Tracker")


    # Label and dropdown for type
    tk.Label(root, text="Type of Item: ").grid(row= 0, column=0, padx= 10, pady= 10)
    type_var = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable = type_var)
    type_dropdown['values'] = ('Credit Card', 'Debit Card', 'Cash')
    type_dropdown.grid(row=0, column= 1, padx= 10, pady=10)


    # labels and entries for name, date, and amount
    tk.Label(root, text="Name: ").grid(row=1, column=0, padx= 10, pady=10)
    name_entry = tk.Entry(root)
    name_entry.grid(row= 1, column=1, padx=10, pady=10)

    tk.Label(root, text="Date (DD-MM-YYYY): ").grid(row=2, column=0, padx= 10, pady=10)
    date_entry = tk.Entry(root)
    date_entry.grid(row= 2, column=1, padx=10, pady=10)

    tk.Label(root, text="Amount: ").grid(row=3, column=0, padx= 10, pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row= 3, column=1, padx=10, pady=10)

    # submit button
    submit_button = tk.Button(root, text= "Add Expense", command=submit_expense)
    submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    # delete button
    delete_button = tk.Button(root, text=" Delete Expense", command=delete_expense)
    delete_button.grid(row= 4, column=2, padx= 10, pady=20)

    # creates a Treeview widget for displaying expenses
    columns = ('Type', 'Name', 'Date', 'Amount')
    tree= ttk.Treeview(root, columns=columns, show='headings')
    tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # define column headings
    for col in columns:
        tree.heading(col, text=col)

    root.mainloop()




def main():
    expenses= []

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")

        choice = input ("Enter your choice; ")


        if choice == '1':
            add_exp_gui(expenses)
        elif choice == '2':
            display_exp(expenses)
        elif choice == '3':
            print("Exiting the program, Goodbye!")
            break
        else: 
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    add_exp_gui()