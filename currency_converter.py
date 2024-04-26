from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = float(input("Enter the Amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

result = c.convert(from_currency, to_currency, amount)
print(result)
