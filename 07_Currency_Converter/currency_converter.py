print("======== CURRENCY CONVERTER ========")

# Show fixed exchange rates

usd_to_eur = 0.87
usd_to_inr = 95.45
usd_to_pkr = 277.42

print("=== Simple Currency Converter ===")
print("Supported currencies: USD, EUR, INR, PKR")

# Take input from the user

amount = float(input("Enter the amount: "))
from_currency = input("Convert from (USD/EUR/INR/PKR): ").upper()
to_currency = input("Convert to (USD/EUR/INR/PKR): ").upper()

# Convert the amount to USD first

if from_currency == "USD":
    amount_in_usd = amount
elif from_currency == "EUR":
    amount_in_usd = amount / usd_to_eur
elif from_currency == "INR":
    amount_in_usd = amount / usd_to_inr
elif from_currency == "PKR":
    amount_in_usd = amount / usd_to_pkr
else:
    print("Invalid currency entered.")
    amount_in_usd = None

# Convert from USD to the target currency

if amount_in_usd is not None:
    if to_currency == "USD":
        result = amount_in_usd
    elif to_currency == "EUR":
        result = amount_in_usd * usd_to_eur
    elif to_currency == "INR":
        result = amount_in_usd * usd_to_inr
    elif to_currency == "PKR":
        result = amount_in_usd * usd_to_pkr
    else:
        print("Invalid currency entered.")
        result = None

    # Show the result

    if result is not None:
        print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")
