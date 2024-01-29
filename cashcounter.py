import pandas as pd
import time

def add_entry(batch_number):
    """
    Take user inputs for a new entry and create a dictionary representing the entry.

    Returns:
        dict: Dictionary representing the new entry.
    """
    # Take user inputs for a new entry
    day = input("Enter the day: ")
    month = input("Enter the month: ")
    person = input("Enter the person: ")
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
    # Get Batch Number
    batch_number =  time.strftime("%Y%m%d%H%M%S")

    # Read the existing Excel file into a DataFrame
    #excel_file_path = "path/to/your/existing_excel_file.xlsx"  # Replace with the actual file path
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
