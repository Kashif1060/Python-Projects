print("===== TEMPERATURE CONVERTER =====")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
convert_to_fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius} Celsius is equal to {convert_to_fahrenheit} Fahrenheit")

# Fahrenheit to Celsius
fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
convert_to_celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} Fahrenheit is equal to {convert_to_celsius} Celsius")
