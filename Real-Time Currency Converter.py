import requests

class CurrencyConverter:
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()
        if "rates" in data:
            self.rates = data["rates"]
        else:
            print("Failed to retrieve exchange rates from the API. Please check your API key.")

    def convert(self, from_currency, to_currency, amount):
        try:
            initial_amount = amount
            if from_currency != 'EUR':
                amount = amount / self.rates[from_currency]

            last_amount = round(amount * self.rates[to_currency], 2)
            print('{} {} = {} {}'.format(initial_amount, from_currency, last_amount, to_currency))
        except KeyError:
            print("Invalid currency entered or failed to update exchange rates from the API.")


url = 'http://data.fixer.io/api/latest?access_key=a7faee89fbb10b1cb5c54fa001d77abb'

c = CurrencyConverter(url)

from_country = input("From Currency: ").upper()
to_country = input("To Currency: ").upper()
try:
    amount = float(input("Amount: "))
    c.convert(from_country, to_country, amount)
except ValueError:
    print("Please enter a valid amount.")
