import pandas as pd
import time
import calendar

def get_batch_number() -> int:
    # Get Batch Number
    return  time.strftime("%Y%m%d")

def get_day(month_str: str) -> int:
    """
    Get a valid day input from the user based on the specified month.

    Args:
        month_str (str): The name of the month.

    Returns:
        int: The selected day.

    Notes:
        The function prompts the user to enter a day and validates if the entered day
        is within the valid range for the specified month. It uses a dictionary to map
        each month to its maximum number of days. If the entered day is not valid, the
        user is prompted to enter a valid day until a valid input is provided.

    Example:
        >>> month_input = input("Enter the month: ")
        >>> day_input = get_day(month_input)
        >>> print(f"Selected day: {day_input}")
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

    Notes:
        The function prompts the user to choose a month by entering the corresponding
        number (1 for January, 2 for February, etc.). It validates the input to ensure
        it is a valid number within the range 1 to 12.

    Example:
        >>> month_input = get_month()
        >>> print(f"Selected month: {month_input}")
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
    people_set = {'Jay', 'Manuel', 'Alejandro', 'Nat', 'Jose', 'Kandy'}
    return people_set

def get_person(people_set: set) -> str:
    """
    Get a valid person input from the user based on the provided set of names.

    Args:
        people_set (set): The set of valid person names.

    Returns:
        str: The selected person.

    Notes:
        The function prompts the user to choose a person by entering the corresponding
        number (1 for the first person, 2 for the second person, etc.). It validates the
        input to ensure it is a valid number within the range of available people.

    Example:
        >>> people_set = {'Jay', 'Manuel', 'Alejandro', 'Nat', 'Jose', 'Kandy'}
        >>> person_input = get_person(people_set)
        >>> print(f"Selected person: {person_input}")
    """
    while True:
        print("Select a person:")
        # Display people with assigned numbers
        for i, person in enumerate(people_set, start=1):
            print(f"{i}. {person}", end='\t')
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



def add_entry(batch_number):
    """
    Take user inputs for a new entry and create a dictionary representing the entry.

    Returns:
        dict: Dictionary representing the new entry.
    """
    # Take user inputs for a new entry
    month =get_month()
    day = get_day(month) 
    person = get_person(get_person_list())
    dept = input("Enter the department: ")

    
    # Take input for each denomination of bills
    bills = [int(input(f"Enter the number of ${value} bills: ")) for value in [100, 50, 20, 10, 5, 2, 1]]

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

def main():
    batch_number = get_batch_number()
    # Read the existing Excel file into a DataFrame
    #excel_file_path = "path/to/your/22existing_excel_file.xlsx"  # Replace with the actual file path
    #df = read_existing_data(excel_file_path)

    # Display the original DataFrame
    #display_data(df)

    # Add a new entry to the DataFrame
    new_entry = add_entry(batch_number=batch_number)
    print (new_entry)
    #df = df.append(new_entry, ignore_index=True)

    # Display the updated DataFrame
    # display_data(df)

    # Save the updated DataFrame back to the Excel file
    #save_data(df, excel_file_path)

if __name__ == "__main__":
    main()
