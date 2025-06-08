from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtain and print the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date():
    """
    Prompt for a number of days, add to today’s date, and print the result in YYYY-MM-DD format.
    """
    try:
        days_str = input("Enter the number of days to add to the current date: ").strip()
        days = int(days_str)
    except ValueError:
        print(f"Invalid input (‘{days_str}’). Please enter an integer.")
        return

    future_date = datetime.now() + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
