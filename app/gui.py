import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, messagebox
import time
from cashCounter import *

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.geometry("400x300")

        self.batch_number = get_batch_number(int(time.strftime("%Y%m%d")), first_run=True)

        self.create_widgets()

    def create_widgets(self):
        # Batch Number
        self.batch_label = tk.Label(self, text=f"Batch Number: {self.batch_number}")
        self.batch_label.pack()

        # Menu Buttons
        self.new_entry_button = tk.Button(self, text="Make a New Entry", command=self.make_new_entry)
        self.new_entry_button.pack(pady=5)

        self.close_batch_button = tk.Button(self, text="Close Batch", command=self.close_batch)
        self.close_batch_button.pack(pady=5)

        self.new_batch_button = tk.Button(self, text="Get New Batch Number", command=self.get_new_batch)
        self.new_batch_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

    def make_new_entry(self):
        self.withdraw()  # Hide main window while taking input
        entry_window = EntryWindow(self.batch_number)
        self.wait_window(entry_window)  # Wait for entry window to close
        self.deiconify()  # Restore main window after entry window is closed

    def close_batch(self):
        clear_screen()
        calculate_bills(str(self.batch_number) + ".csv")
        calculate_amounts(str(self.batch_number) + ".csv")
        calculate_total_amount(str(self.batch_number) + ".csv")
        self.batch_number = get_batch_number(self.batch_number)
        messagebox.showinfo("Batch Closed", f"Batch closed. New batch number: {self.batch_number}")

    def get_new_batch(self):
        self.batch_number = get_batch_number(self.batch_number)
        self.batch_label.config(text=f"Batch Number: {self.batch_number}")
        messagebox.showinfo("New Batch Number", f"New batch number: {self.batch_number}")
class EntryWindow(tk.Toplevel):
    def __init__(self, batch_number):
        super().__init__()

        self.title("New Entry")
        self.geometry("400x300")

        self.batch_number = batch_number

        self.create_widgets()

    def create_widgets(self):
        # Month
        self.month_label = tk.Label(self, text="Month:")
        self.month_label.pack()

        self.month_var = tk.StringVar(self)
        self.month_dropdown = ttk.Combobox(self, textvariable=self.month_var)
        self.month_dropdown['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        )
        self.month_dropdown.pack()

        # Day
        self.day_label = tk.Label(self, text="Day:")
        self.day_label.pack()

        self.day_var = tk.StringVar(self)
        self.day_dropdown = ttk.Combobox(self, textvariable=self.day_var)
        self.day_dropdown['values'] = tuple(range(1, 32))
        self.day_dropdown.pack()

        # Person
        self.person_label = tk.Label(self, text="Person:")
        self.person_label.pack()

        self.person_var = tk.StringVar(self)
        self.person_dropdown = ttk.Combobox(self, textvariable=self.person_var)
        self.person_dropdown['values'] = get_person_list()
        self.person_dropdown.pack()

        # Department
        self.department_label = tk.Label(self, text="Department:")
        self.department_label.pack()

        self.department_var = tk.StringVar(self)
        self.department_dropdown = ttk.Combobox(self, textvariable=self.department_var)
        self.department_dropdown['values'] = dept_lst()
        self.department_dropdown.pack()

        # Bills
        self.bills_label = tk.Label(self, text="Bills (comma-separated):")
        self.bills_label.pack()

        self.bills_entry = tk.Entry(self)
        self.bills_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_entry)
        self.submit_button.pack(pady=5)

    def submit_entry(self):
        month = self.month_var.get()
        day = self.day_var.get()
        person = self.person_var.get()
        department = self.department_var.get()
        bills = self.bills_entry.get()

        # Validate inputs
        if not all((month, day, person, department, bills)):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            day = int(day)
            bills = list(map(int, bills.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Invalid input format")
            return

        new_entry = {
            'Batch Number': self.batch_number,
            'Day': day,
            'Month': month,
            'Person': person,
            'Dept': department,
            100: bills[0],
            50: bills[1],
            20: bills[2],
            10: bills[3],
            5: bills[4],
            2: bills[5],
            1: bills[6],
            'Total Bills': sum(bills),
            'Total Amount': sum(bill * value for bill, value in zip(bills, [100, 50, 20, 10, 5, 2, 1]))
        }

        append_entry_to_csv(new_entry, str(self.batch_number) + ".csv")
        messagebox.showinfo("Success", "Entry added successfully")
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
