import pandas as pd
import time
import calendar
import os
import platform

def clear_screen():
    """Clear the terminal screen."""
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def get_batch_number() -> int:
    """Get a unique batch number based on the current timestamp."""
    return int(time.strftime("%Y%m%d%S"))

def get_day(month_str: str) -> int:
    """
    Get a valid day input from the user based on the specified month.

    Args:
        month_str (str): The name of the month.

    Returns:
        int: The selected day.
    """
    while True:
        day = int(input("Enter the day: "))
        days_in_month = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        }
        max_days = days_in_month.get(month_str, None)

        if max_days is not None and 1 <= day <= max_days:
            break
        else:
            print("Please enter a valid day for the specified month.")

    return day

def get_month() -> str:
    """
    Get a valid month input from the user.

    Returns:
        str: The selected month.
    """
    while True:
        print("Select a month:")
        max_month_length = max(len(month) for month in calendar.month_name[1:])
        for month_number in range(1, 13):
            print(f"{month_number}. {calendar.month_name[month_number]: <{max_month_length + 2}}", end='\t')
            if month_number % 6 == 0:
                print()

        try:
            month_number = int(input("\nEnter the number for the month: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= month_number <= 12:
            months = {
                1: 'January',
                2: 'February',
                3: 'March',
                4: 'April',
                5: 'May',
                6: 'June',
                7: 'July',
                8: 'August',
                9: 'September',
                10: 'October',
                11: 'November',
                12: 'December'
            }
            selected_month = months[month_number]
            return selected_month
        else:
            print("Please enter a valid number between 1 and 12.")

def get_person_list() -> set:
    """Get a set of valid person names."""
    return {'Jay', 'Manuel', 'Alejandro', 'Nat', 'Jose', 'Kandy', 'Raheel'}

def get_person(people_set: set) -> str:
    """
    Get a valid person input from the user based on the provided set of names.

    Args:
        people_set (set): The set of valid person names.

    Returns:
        str: The selected person.
    """
    while True:
        print("Select a person:")
        max_name_length = max(len(name) for name in people_set)
        for i, person in enumerate(people_set, start=1):
            print(f"{i}. {person: <{max_name_length}}", end='\t')
            if i % 6 == 0:
                print()

        try:
            person_number = int(input("\nEnter the number for the person: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= person_number <= len(people_set):
            selected_person = list(people_set)[person_number - 1]
            return selected_person
        else:
            print("Please enter a valid number within the range of available people.")

def dept_lst() -> set:
    """Get a set of valid department names."""
    return {'Store', 'Car Wash'}

def get_department(department_set: set) -> str:
    """
    Get a valid department input from the user based on the provided set of names.

    Args:
        department_set (set): The set of valid department names.

    Returns:
        str: The selected department.
    """
    while True:
        print("Select a department:")
        max_name_length = max(len(name) for name in department_set)
        for i, department in enumerate(department_set, start=1):
            print(f"{i}. {department: <{max_name_length}}", end='\t')
            if i % 6 == 0:
                print()

        try:
            department_number = int(input("\nEnter the number for the department: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= department_number <= len(department_set):
            selected_department = list(department_set)[department_number - 1]
            return selected_department
        else:
            print("Please enter a valid number within the range of available departments.")

def add_entry(batch_number):
    """Take user inputs for a new entry and create a dictionary representing the entry."""
    month = get_month()
    print(f"You selected '{month}'")
    time.sleep(1)
    clear_screen()

    day = get_day(month)
    print(f"You selected '{day}'")
    time.sleep(1)
    clear_screen()

    person = get_person(get_person_list())
    print(f"You selected '{person}'")
    time.sleep(1)
    clear_screen()

    dept = get_department(department_set=dept_lst())
    print(f"You selected '{dept}'")
    time.sleep(1)
    clear_screen()

    bills = []
    for value in [100, 50, 20, 10, 5, 2, 1]:
        while True:
            try:
                bill_count = int(input(f"Enter the number of ${value} bills: "))
                bills.append(bill_count)
                break
            except ValueError:
                print("Invalid entry. Please enter a valid integer.")

    total_bills = sum(bills)
    total_amount = sum([bill * value for bill, value in zip(bills, [100, 50, 20, 10, 5, 2, 1])])

    new_entry = {
        'Batch Number': batch_number,
        'Day': day,
        'Month': month,
        'Person': person,
        'Dept': dept,
        100: bills[0],
        50: bills[1],
        20: bills[2],
        10: bills[3],
        5: bills[4],
        2: bills[5],
        1: bills[6],
        'Total Bills': total_bills,
        'Total Amount': total_amount
    }

    return new_entry

def calculate_agk_columns(df):
    """Calculate AGK entry columns: Gas Cash, Net Merch Sales, Merch Cash, Total Cash, Short/Over, and Status."""
    df['Gas Cash'] = df.apply(lambda row: row['Gas CC'] if row['Shift'] == 1 else row['Gas CC'] - df.loc[(df['Day'] == row['Day']) & (df['Month'] == row['Month']) & (df['Shift'] == 1), 'Gas Cash'].values[0], axis=1)
    df['Net Merch Sales'] = df['Tot Merch Sales'] + df['Sales Tax']
    df['Merch Cash'] = df.apply(lambda row: row['Merch CC'] if row['Shift'] == 1 else row['Merch CC'] - df.loc[(df['Day'] == row['Day']) & (df['Month'] == row['Month']) & (df['Shift'] == 1), 'Merch Cash'].values[0], axis=1)
    df['Total Cash'] = df['Gas Cash'] + df['Merch Cash'] - df['Payouts']
    df['Short/Over'] = df['Actual Cash'] - df['Total Cash']
    df['Status'] = df['Short/Over'].apply(lambda x: 'Over' if x >= 0 else 'Short')

def read_existing_data(excel_file_path):
    """Read the existing Excel file into a DataFrame."""
    df = pd.read_excel(excel_file_path)
    return df

def display_data(df):
    """Display the DataFrame."""
    print("DataFrame:")
    print(df)

def save_data(df, excel_file_path):
    """Save the DataFrame back to the Excel file."""
    df.to_excel(excel_file_path, index=False)
    print("Data saved successfully.")

def append_entry_to_csv(new_entry: dict, csv_file):
    """Append a new entry to a CSV file."""
    entry_df = pd.DataFrame([new_entry])
    if os.path.exists(csv_file):
        entry_df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        entry_df.to_csv(csv_file, mode='a', header=True, index=False)

def get_csv_header():
    """Get the CSV header."""
    return ["Batch Number", "Day", "Month", "Shift", "Person", "Actual Cash", "Total Gas Sold", "Gas CC", "Gas Cash",
            "Tot Merch Sales", "Sales Tax", "Net Merch Sales", "Merch CC", "Merch Cash", "Payouts", "Total Cash",
            "Short/Over", "Status"]

def get_file_name() -> str:
    """Prompt the user for a file name, check if the file exists, and create it if needed."""
    while True:
        file_name = input("Enter a CSV file name (without extension): ") + ".csv"
        if os.path.exists(file_name):
            print(f"Found file: '{file_name}'.")
            break
        else:
            with open(file_name, 'w'):
                pass
            print(f"File '{file_name}' created.")
            break

    return file_name
def take_action(batch_number: int, cash_df, agk_df):
    """Main function to take user actions."""
    while True:
        print("*" * 50)
        print("Welcome to the Application!")
        print(f"1. Get New Batch Number: Your current batch number is {batch_number}")
        print("2. Make a New Entry for Cash Collection")
        print("3. Make a New AGK Entry")
        print("4. Write Cash Collection to file")
        print("5. Write AGK Entry to file")
        print("6. Exit")
        print("*" * 50)

        choice = input("Enter your choice: ")

        if choice == '1':
            batch_number = get_batch_number()
        elif choice == '2':
            new_entry = add_entry(batch_number=batch_number)
            append_entry_to_csv(new_entry=new_entry, csv_file='cash_collection.csv')
        elif choice == '3':
            # Prompt user for AGK Entry information
            agk_entry = {}
            agk_entry['Day'] = int(input("Enter the day: "))
            agk_entry['Month'] = input("Enter the month: ")
            agk_entry['Shift'] = int(input("Enter the shift (1 or 2): "))
            agk_entry['Person'] = input("Enter the person: ")
            agk_entry['Actual Cash'] = float(input("Enter the actual cash: "))
            agk_entry['Total Gas Sold'] = float(input("Enter the total gas sold: "))
            agk_entry['Gas CC'] = float(input("Enter the gas CC: "))
            agk_entry['Tot Merch Sales'] = float(input("Enter the total merchandise sales: "))
            agk_entry['Sales Tax'] = float(input("Enter the sales tax: "))
            agk_entry['Merch CC'] = float(input("Enter the merchandise CC: "))
            agk_entry['Payouts'] = float(input("Enter the payouts: "))

            # Check if agk_df is None and create it
            if agk_df is None:
                agk_df = pd.DataFrame(columns=['Day', 'Month', 'Shift', 'Person', 'Actual Cash', 'Total Gas Sold',
                                               'Gas CC', 'Tot Merch Sales', 'Sales Tax', 'Merch CC', 'Payouts'])

            # Append AGK entry to DataFrame
            agk_df = pd.concat([agk_df, pd.DataFrame([agk_entry])], ignore_index=True)
            # Calculate AGK columns
            calculate_agk_columns(agk_df)
        elif choice == '4':
            file = get_file_name()
            append_entry_to_csv(new_entry=new_entry, csv_file=file)
        elif choice == '5':
            agk_file = get_file_name()
            agk_df.to_csv(agk_file, index=False)
        elif choice == '6':
            break
        else:
            print(f"{choice} is an invalid entry")

    return batch_number, cash_df, agk_df


def take_action2(batch_number: int, cash_df, agk_df):
    """Main function to take user actions."""
    while True:
        print("*" * 50)
        print("Welcome to the Application!")
        print(f"1. Get New Batch Number: Your current batch number is {batch_number}")
        print("2. Make a New Entry for Cash Collection")
        print("3. Make a New AGK Entry")
        print("4. Write Cash Collection to file")
        print("5. Write AGK Entry to file")
        print("6. Exit")
        print("*" * 50)

        choice = input("Enter your choice: ")

        if choice == '1':
            batch_number = get_batch_number()
        elif choice == '2':
            new_entry = add_entry(batch_number=batch_number)
            append_entry_to_csv(new_entry=new_entry, csv_file='cash_collection.csv')
        elif choice == '3':
            # Prompt user for AGK Entry information
            agk_entry = {}
            agk_entry['Day'] = int(input("Enter the day: "))
            agk_entry['Month'] = input("Enter the month: ")
            agk_entry['Shift'] = int(input("Enter the shift (1 or 2): "))
            agk_entry['Person'] = input("Enter the person: ")
            agk_entry['Actual Cash'] = float(input("Enter the actual cash: "))
            agk_entry['Total Gas Sold'] = float(input("Enter the total gas sold: "))
            agk_entry['Gas CC'] = float(input("Enter the gas CC: "))
            agk_entry['Tot Merch Sales'] = float(input("Enter the total merchandise sales: "))
            agk_entry['Sales Tax'] = float(input("Enter the sales tax: "))
            agk_entry['Merch CC'] = float(input("Enter the merchandise CC: "))
            agk_entry['Payouts'] = float(input("Enter the payouts: "))

            # Append AGK entry to DataFrame
            agk_df = agk_df.append(agk_entry, ignore_index=True)
            # Calculate AGK columns
            calculate_agk_columns(agk_df)
        elif choice == '4':
            file = get_file_name()
            append_entry_to_csv(new_entry=new_entry, csv_file=file)
        elif choice == '5':
            agk_file = get_file_name()
            agk_df.to_csv(agk_file, index=False)
        elif choice == '6':
            break
        else:
            print(f"{choice} is an invalid entry")

    return batch_number

def main():
    clear_screen()
    batch_number = get_batch_number()
    # Read the existing data for AGK Entry
    agk_file_path = "agk_entry.csv"  # Replace with the actual file path
    agk_df = pd.read_csv(agk_file_path) if os.path.exists(agk_file_path) else pd.DataFrame(columns=get_csv_header())
    # Read the existing data for Cash Collection
    cash_file_path = "cash_collection.csv"  # Replace with the actual file path
    cash_df = pd.read_csv(cash_file_path) if os.path.exists(cash_file_path) else pd.DataFrame(columns=get_csv_header())

    batch_number = take_action(batch_number=batch_number, cash_df=cash_df, agk_df=agk_df)

    # Save the updated AGK DataFrame back to the AGK Entry file
    agk_file_path = "agk_entry.csv"  # Replace with the actual file path
    agk_df.to_csv(agk_file_path, index=False)
    print("AGK Entry data saved successfully.")

    # Save the updated Cash Collection DataFrame back to the Cash Collection file
    cash_file_path = "cash_collection.csv"  # Replace with the actual file path
    cash_df.to_csv(cash_file_path, index=False)
    print("Cash Collection data saved successfully.")

if __name__ == "__main__":
    main()
