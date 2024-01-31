import pandas as pd
import time
import calendar
import os
import platform

def clear_screen():
    """
    Clear the console screen.
    """
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def get_batch_number() -> int:
    """
    Generate and return a new batch number based on the current date and time.
    """
    return time.strftime("%Y%m%d%S")

def get_day(month_str: str) -> int:
    """
    Get a valid day input from the user based on the specified month.

    Args:
        month_str (str): The name of the month.

    Returns:
        int: The selected day.
    """
    while True:
        day = int(input("Enter the day: "))  # Convert the input to an integer

        # Define a dictionary to map each month to its corresponding maximum number of days
        days_in_month = {
            'January': 31,
            'February': 28,  # You may need to adjust this for leap years
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

        # Use the month string to get the maximum number of days
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
        # Display months with adjusted width for the longest month name
        max_month_length = max(len(month) for month in calendar.month_name[1:])
        for month_number in range(1, 13):
            print(f"{month_number}. {calendar.month_name[month_number]: <{max_month_length + 2}}", end='\t')
            if month_number % 6 == 0:
                print()  # Start a new line after every 6 months

        try:
            month_number = int(input("\nEnter the number for the month: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= month_number <= 12:
            # Use a dictionary to map month numbers to month names
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
    """
    Get a set of valid person names.

    Returns:
        set: Set of person names.
    """
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
        # Display people with adjusted width for the longest name
        max_name_length = max(len(name) for name in people_set)
        for i, person in enumerate(people_set, start=1):
            print(f"{i}. {person: <{max_name_length}}", end='\t')
            if i % 6 == 0:
                print()  # Start a new line after every 6 people

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
    """
    Get a set of valid department names.

    Returns:
        set: Set of department names.
    """
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
        # Display departments with adjusted width for the longest name
        max_name_length = max(len(name) for name in department_set)
        for i, department in enumerate(department_set, start=1):
            print(f"{i}. {department: <{max_name_length}}", end='\t')
            if i % 6 == 0:
                print()  # Start a new line after every 6 departments

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

def add_cash_collection_entry(batch_number):
    """
    Take user inputs for a new cash collection entry and create a dictionary representing the entry.

    Args:
        batch_number (str): Batch number associated with the entry.

    Returns:
        dict: Dictionary representing the new cash collection entry.
    """
    # Take user inputs for a new entry
    
    # Get month
    month = get_month()
    print(f"You selected '{month}'")
    time.sleep(1)
    clear_screen()
    
    # Get day
    print(f"Month: {month}\n")
    day = get_day(month)
    print(f"You selected '{day}'")
    time.sleep(1)
    clear_screen()
    
    # Get person
    print(f"Month: {month}, Day: {day}\n")
    person = get_person(get_person_list())
    print(f"You selected '{person}'")
    time.sleep(1)
    clear_screen()
    
    # Get department
    print(f"Month: {month}, Day: {day}, Person: {person}\n")
    dept = get_department(department_set=dept_lst())
    print(f"You selected '{dept}'")
    time.sleep(1)
    clear_screen()
    
    # Take input for each denomination of bills
    print(f"Month: {month}, Day: {day}, Person: {person}, Department: {dept}\n")

    bills = []

    for value in [100, 50, 20, 10, 5, 2, 1]:
        while True:
            try:
                bill_count = int(input(f"Enter the number of ${value} bills: "))
                bills.append(bill_count)
                break  # Exit the loop if the input is a valid integer
            except ValueError:
                print("Invalid entry. Please enter a valid integer.")

    total_bills = sum(bills)
    total_amount = sum([bill * value for bill, value in zip(bills, [100, 50, 20, 10, 5, 2, 1])])

    # Create a new entry as a dictionary
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
        'Total Amount': f"${total_amount:,.2f}"  # Format total amount as currency
    }

    # Add calculated columns
    new_entry['Gas Cash'] = new_entry[100] - new_entry[50] - new_entry[20] - new_entry[10] - new_entry[5] - new_entry[2] - new_entry[1]
    new_entry['Net Merch Sales'] = new_entry[20] + new_entry[10]
    new_entry['Merch Cash'] = new_entry[50] - new_entry[20] - new_entry[10] - new_entry[5] - new_entry[2] - new_entry[1]
    new_entry['Total Cash'] = new_entry[20] + new_entry[10] - new_entry['Merch Cash']
    new_entry['Short/Over'] = new_entry[100] - new_entry[50] - new_entry[20] - new_entry[10] - new_entry[5] - new_entry[2] - new_entry[1] - new_entry['Total Cash']
    new_entry['Status'] = 'Over' if new_entry['Short/Over'] >= 0 else 'Short'

    return new_entry

def add_agk_entry(batch_number):
    """
    Take user inputs for a new AGK entry and create a dictionary representing the entry.

    Args:
        batch_number (str): Batch number associated with the entry.

    Returns:
        dict: Dictionary representing the new AGK entry.
    """
    print("Enter AGK entry details:")
    # Get day
    day = int(input("Enter the day: "))
    
    # Get month
    month = input("Enter the month: ")
    
    # Get shift
    shift = int(input("Enter the shift: "))
    
    # Get person
    person = input("Enter the person: ")
    
    # Get actual cash
    actual_cash = float(input("Enter the actual cash: "))
    
    # Get total gas sold
    total_gas_sold = float(input("Enter the total gas sold: "))
    
    # Get gas CC
    gas_cc = float(input("Enter the gas CC: "))
    
    # Get gas cash
    gas_cash = float(input("Enter the gas cash: "))
    
    # Get total merch sales
    total_merch_sales = float(input("Enter the total merch sales: "))
    
    # Get sales tax
    sales_tax = float(input("Enter the sales tax: "))
    
    # Get net merch sales
    net_merch_sales = float(input("Enter the net merch sales: "))
    
    # Get merch CC
    merch_cc = float(input("Enter the merch CC: "))
    
    # Get merch cash
    merch_cash = float(input("Enter the merch cash: "))
    
    # Get payouts
    payouts = float(input("Enter the payouts: "))
    
    # Get total cash
    total_cash = float(input("Enter the total cash: "))
    
    # Get short/over
    short_over = float(input("Enter the short/over: "))
    
    # Get status
    status = input("Enter the status (Over/Short): ")

    # Create a new entry as a dictionary
    new_entry = {
        'Batch Number': batch_number,
        'Day': day,
        'Month': month,
        'Shift': shift,
        'Person': person,
        'Actual Cash': actual_cash,
        'Total Gas Sold': total_gas_sold,
        'Gas CC': gas_cc,
        'Gas Cash': gas_cash,
        'Tot Merch Sales': total_merch_sales,
        'Sales Tax': sales_tax,
        'Net Merch Sales': net_merch_sales,
        'Merch CC': merch_cc,
        'Merch Cash': merch_cash,
        'Payouts': payouts,
        'Total Cash': total_cash,
        'Short/Over': short_over,
        'Status': status
    }

    return new_entry

def read_existing_data(excel_file_path):
    """
    Read the existing Excel file into a DataFrame.

    Args:
        excel_file_path (str): Path to the existing Excel file.

    Returns:
        pd.DataFrame: DataFrame containing existing data.
    """
    df = pd.read_excel(excel_file_path)
    return df

def display_data(df):
    """
    Display the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to be displayed.
    """
    print("DataFrame:")
    print(df)

def save_data(df, excel_file_path):
    """
    Save the DataFrame back to the Excel file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        excel_file_path (str): Path to the Excel file.
    """
    df.to_excel(excel_file_path, index=False)
    print("Data saved successfully.")

def menu(batch_number) -> int:
    """
    Display the menu and get the user's choice.

    Args:
        batch_number (int): The current batch number.

    Returns:
        int: User's choice.
    """
    print("*" * 50)
    print("Welcome to the Application!")
    print(f"1. Get New Batch Number: Your current batch number is {batch_number}")
    print("2. Make a New Cash Collection Entry")
    print("3. Make a New AGK Entry")
    print("4. Write to file")
    print("5. Exit")
    print("*" * 50)
    while True:
        choice = str(input("Enter your choice: "))
        if choice in ['1', '2', '3', '4', '5']:
            clear_screen()
            return int(choice)
        else:
            print(f"{choice}, is an invalid choice. Try again.")
            time.sleep(1)
            clear_screen()

def append_entry_to_csv(new_entry: dict, csv_file):
    """
    Append a new entry to a CSV file.

    Args:
        new_entry (dict): Dictionary representing the new entry.
        csv_file (str): Path to the CSV file to which the entry will be appended.
    """
    # Convert the new entry to a DataFrame
    entry_df = pd.DataFrame([new_entry])

    # Append the entry to the CSV file
    if os.path.exists(csv_file):
        entry_df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        entry_df.to_csv(csv_file, mode='a', header=True, index=False)

def get_csv_header():
    """
    Get the CSV header.

    Returns:
        list: List of header names.
    """
    return ["Batch Number", "Date", "Month", "Person", "Department",
            "100s", "50s", "20s", "10s", "5s", "2s", "1s", "Total Bills", "$Value", "Gas Cash", "Net Merch Sales",
            "Merch Cash", "Total Cash", "Short/Over", "Status"]

def get_file_name() -> str:
    """
    Prompt the user for a file name, check if the file exists, and create it if needed.

    Returns:
        str: The chosen or created file name.
    """
    while True:
        file_name = input("Enter a CSV file name (without extension): ") + ".csv"

        # Check if the file already exists
        if os.path.exists(file_name):
            print(f"Found file: '{file_name}'.")
            break
        else:
            # Create the file if it doesn't exist
            with open(file_name, 'w'):
                pass
            print(f"File '{file_name}' created.")
            break

    return file_name

def take_action(batch_number: int):
    """
    Main function to handle user actions.

    Args:
        batch_number (int): The current batch number.
    """
    while True:
        choice = menu(batch_number=batch_number)
        if choice == 1:
            batch_number = get_batch_number()
        elif choice == 2:
            new_entry = add_cash_collection_entry(batch_number=batch_number)
            print(new_entry)
            _ = input("Enter any key to continue")
            clear_screen()
        elif choice == 3:
            new_entry = add_agk_entry(batch_number=batch_number)
            print(new_entry)
            _ = input("Enter any key to continue")
            clear_screen()
        elif choice == 4:
            file = get_file_name()
            append_entry_to_csv(new_entry=new_entry, csv_file=file)
        elif choice == 5:
            break
        else:
            print(f"{choice} is an invalid entry")

if __name__ == "__main__":
    batch_number = get_batch_number()
    take_action(batch_number=batch_number)
