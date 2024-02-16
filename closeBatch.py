import os
import pandas as pd


def calculate_bills_and_amounts(csv_file: str) -> None:
    # Read the CSVfile into Pandas DataFrame
    df: pd.DataFrame = pd.read_csv(csv_file)

    # Initialize dictionaries to store counts and amounts for each denomination
    bill_counts: dict= {}
    bill_amounts: dict = {}

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # print( index, ", ", row)
        for denomination in [100, 50, 20, 10, 5, 2 , 1]:
            # Calculate total bills for the current denomination
            total_bills: int = row[str(denomination)]
            # print(total_bills)

            # If the denomination is not primed then initialize it 
            if denomination not in bill_counts:
                bill_counts[denomination] = 0
                bill_amounts[denomination] = 0
            
            # Add the total bills and dollar amount for the current denomination
            bill_counts[denomination] += total_bills
            bill_amounts[denomination] += total_bills * denomination
    
    # Add the results to a new row at the end of the DataFrame
    result_row = {'Batch Number': None, 'Date': None, 'Month': None, 'Person': None, 'Department': None}
    for denomination in [100, 50, 20, 10, 5, 2, 1]:
        result_row[str(denomination)] = bill_counts[denomination]
        result_row[f"{denomination}_Value"] = bill_amounts[denomination]
    result_row['Total Bills'] = sum(bill_amounts.values())
    #result_row['$'] = sum(bill_amounts.values())

    df = df._append(result_row, ignore_index=True)

    # Write the updated DataFrame to the original csv file 
    df.to_csv(csv_file, index=False)

def main():
    filename = "20240215.csv"
    calculate_bills_and_amounts(filename)


if __name__ == "__main__":
    main()

    