import requests

def currency_converter(amount, from_currency, to_currency):
    # API endpoint for currency conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Sending HTTP request to the API
    response = requests.get(url)
    data = response.json()

    # Extracting conversion rate from the response
    conversion_rate = data['rates'][to_currency]

    # Calculating the converted amount
    converted_amount = amount * conversion_rate

    return converted_amount

# Taking user input
amount = float(input("Enter the amount to be converted: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

# Calling the currency converter function
converted_amount = currency_converter(amount, from_currency, to_currency)

# Displaying the converted amount
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
