#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

api_key = "0e2d9593210942c2b4f89799f397f8b1"
base_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

def convert_currency(amount, from_currency, to_currency):
    try:
        response = requests.get(base_url)
        exchange_rates = response.json()["rates"]
        from_rate = exchange_rates[from_currency.upper()]
        to_rate = exchange_rates[to_currency.upper()]
    except:
        return "Error: Unable to retrieve exchange rates from API."

    try:
        result = amount * (to_rate / from_rate)
        return round(result, 2)
    except:
        return "Error: Invalid amount entered."

while True:
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency: ")
        to_currency = input("To currency: ")

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")
    except ValueError:
        print("Error: Invalid input entered.")
    except KeyboardInterrupt:
        break


# In[ ]:




