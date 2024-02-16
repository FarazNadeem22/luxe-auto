import os
import pandas as pd


def calculate_bills(csv_file: str) -> None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select only the columns containing bill denominations
    bill_columns = ['100', '50', '20', '10', '5', '2', '1']

    # Calculate the total number of bills for each denomination
    bill_counts = df[bill_columns].sum()

    # Add the total bill counts to a new row at the end of the DataFrame
    total_row = {'Batch Number': None, 'Day': None, 'Month': None, 'Person': None, 'Dept': None}
    for denomination, count in bill_counts.items():
        total_row[str(denomination)] = count
    total_row['Total Bills'] = sum(bill_counts)

    # Append the total row to the DataFrame
    df = df._append(total_row, ignore_index=True)

    # Write the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)


def calculate_amounts(csv_file: str) -> None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select only the columns containing bill denominations
    bill_columns = ['100', '50', '20', '10', '5', '2', '1']

    # Calculate the total amount for each denomination
    bill_amounts = df[bill_columns].multiply([100, 50, 20, 10, 5, 2, 1]).sum()

    # Add the total amount row to the DataFrame
    total_row = {'Batch Number': None, 'Day': None, 'Month': None, 'Person': None, 'Dept': None}
    for denomination, amount in bill_amounts.items():
        total_row[str(denomination)] = amount/2

    # Append the total row to the DataFrame
    df = df._append(total_row, ignore_index=True)

    # Write the updated DataFrame to the original csv file 
    df.to_csv(csv_file, index=False)

def calculate_total_amount(csv_file: str) -> None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select only the columns containing bill denominations
    bill_columns = ['100', '50', '20', '10', '5', '2', '1']

    # Sum the values from the last line for each denomination
    total_amounts = df.iloc[-1][bill_columns].sum()

    # Insert the total amounts into the bottom right corner cell
    df.loc[df.index[-1], 'Total Amount'] = total_amounts

    # Write the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

def main():
    filename = "20240215copy.csv"
    calculate_bills(filename)
    calculate_amounts(filename)
    calculate_total_amount(filename)

if __name__ == "__main__":
    main()

    
    