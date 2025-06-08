# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: (°F − 32) × (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: (°C × (9/5)) + 32
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Prompt for temperature value
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        celsius = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius}°C")
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        fahrenheit = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
