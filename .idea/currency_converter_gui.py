import requests
import tkinter as tk
from tkinter import messagebox

def currency_converter():
    amount = amount_entry.get()
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()

    # Input validation
    if not amount or not from_currency or not to_currency:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
        return

    # API endpoint for currency conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Sending HTTP request to the API
    response = requests.get(url)
    data = response.json()

    # Check if API request was successful
    if response.status_code != 200 or 'rates' not in data:
        messagebox.showerror("Error", "Failed to retrieve currency conversion data.")
        return

    # Check if conversion rate exists
    if to_currency not in data['rates']:
        messagebox.showerror("Error", f"Conversion rate for {to_currency} not found.")
        return

    # Extracting conversion rate from the response
    conversion_rate = data['rates'][to_currency]

    # Calculating the converted amount
    converted_amount = amount * conversion_rate

    # Displaying the converted amount
    messagebox.showinfo("Result", f"{amount} {from_currency} = {converted_amount} {to_currency}")

# Create the GUI window
window = tk.Tk()
window.title("Currency Converter")

# Create labels and entry fields
amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_entry = tk.Entry(window)
from_currency_entry.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_entry = tk.Entry(window)
to_currency_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=currency_converter)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
