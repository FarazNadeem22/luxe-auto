import pandas as pd

def calculate_gas_cash(row):
    """
    Calculate Gas Cash based on the provided formula.

    Parameters:
        row (pd.Series): A Pandas Series representing a row in the DataFrame.

    Returns:
        float: The calculated Gas Cash value.
    """
    if row['Shift'] == 1:
        return row['Total Gas Sold'] - row['Gas CC'] - row['Gas Cash'].shift(1)
    else:
        return row['Total Gas Sold'] - row['Gas CC'] - row['Gas Cash']

def calculate_merch_cash(row):
    """
    Calculate Merch Cash based on the provided formula.

    Parameters:
        row (pd.Series): A Pandas Series representing a row in the DataFrame.

    Returns:
        float: The calculated Merch Cash value.
    """
    if row['Shift'] == 1:
        return row['Net Merch Sales'] - row['Merch CC'] - row['Merch Cash'].shift(1)
    else:
        return row['Net Merch Sales'] - row['Merch CC'] - row['Merch Cash']

def calculate_total_cash(row):
    """
    Calculate Total Cash based on the provided formula.

    Parameters:
        row (pd.Series): A Pandas Series representing a row in the DataFrame.

    Returns:
        float: The calculated Total Cash value.
    """
    return row['Gas Cash'] + row['Merch Cash']

def calculate_short_over(row):
    """
    Calculate Short/Over based on the provided formula.

    Parameters:
        row (pd.Series): A Pandas Series representing a row in the DataFrame.

    Returns:
        float: The calculated Short/Over value.
    """
    return row['Actual Cash'] - row['Total Cash']

def calculate_status(row):
    """
    Calculate Status based on the provided formula.

    Parameters:
        row (pd.Series): A Pandas Series representing a row in the DataFrame.

    Returns:
        str: The calculated Status value ('Over' or 'Short').
    """
    return 'Over' if row['Short/Over'] >= 0 else 'Short'

def main():
    """
    Collect user input for each column, calculate missing columns, and display the final DataFrame.
    """
    # Get user input for columns A to R
    data = {
        'Sr No': [],
        'Day': [],
        'Month': [],
        'Shift': [],
        'Person': [],
        'Actual Cash': [],
        'Total Gas Sold': [],
        'Gas CC': [],
        'Gas Cash': [],
        'Tot Merch Sales': [],
        'Sales Tax': [],
        'Net Merch Sales': [],
        'Merch CC': [],
        'Merch Cash': [],
        'Payouts': [],
        'Total Cash': [],
        'Short/Over': [],
        'Status': []
    }

    # Collect user input for each column
    for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']:
        data[col] = [float(input(f"Enter {col}: ")) for _ in range(len(data['Sr No']))]

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Calculate missing columns
    df['Gas Cash'] = df.apply(calculate_gas_cash, axis=1)
    df['Net Merch Sales'] = df['Tot Merch Sales'] + df['Sales Tax']
    df['Merch Cash'] = df.apply(calculate_merch_cash, axis=1)
    df['Total Cash'] = df.apply(calculate_total_cash, axis=1)
    df['Short/Over'] = df.apply(calculate_short_over, axis=1)
    df['Status'] = df.apply(calculate_status, axis=1)

    # Display the final DataFrame
    print(df)

if __name__ == "__main__":
    main()
