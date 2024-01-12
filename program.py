import pandas as pd

def check_employees(file_path):
    # Load the spreadsheet into a Pandas DataFrame
    df = pd.read_csv(file_path)  

    # Sort the data by employee and date
    df.sort_values(by=['Employee Name', 'Time'], inplace=True)

    
    consecutive_days = 0
    prev_end_time = None

    # Iterate through the DataFrame to analyze employees
    for index, row in df.iterrows():
        current_employee = row['Employee Name']
        current_position = row['Position ID']
        current_start_time = pd.to_datetime(row['Time'])
        current_end_time = pd.to_datetime(row['Time Out'])

        # Condition a) Check for 7 consecutive days
        if prev_end_time is not None and (current_start_time - prev_end_time).days == 1:
            consecutive_days += 1
        else:
            consecutive_days = 0

        if consecutive_days == 6:  # 7 consecutive days (including the current day)
            print(f"Employee: {current_employee}, Position ID: {current_position} - Worked for 7 consecutive days")

        # Condition b) Check for less than 10 hours between shifts but greater than 1 hour
        time_between_shifts = current_start_time - prev_end_time if prev_end_time is not None else None
        if time_between_shifts is not None and 1 < time_between_shifts.total_seconds() // 3600 < 10:
            print(f"Employee: {current_employee}, Position ID: {current_position} - Less than 10 hours between shifts")

        # Condition c) Check for more than 14 hours in a single shift
        if (current_end_time - current_start_time).total_seconds() // 3600 > 14:
            print(f"Employee: {current_employee}, Position ID: {current_position} - Worked more than 14 hours in a single shift")

        # Update previous end time for the next iteration
        prev_end_time = current_end_time

if __name__ == "__main__":
    file_path = r"C:\Users\KIIT\Desktop\test\Assignment.csv"  
    check_employees(file_path)
