import random

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        change_percent = random.uniform(-0.1, 0.1)
        self.price = round(self.price * (1 + change_percent), 2)

class Market:
    def __init__(self):
        self.stocks = {
            'ABC': Stock('ABC', 100.0),
            'XYZ': Stock('XYZ', 150.0),
            'LMN': Stock('LMN', 75.0)
        }

    def update_prices(self):
        for stock in self.stocks.values():
            stock.update_price()

    def show_prices(self):
        print("\nCurrent Market Prices:")
        for stock in self.stocks.values():
            print(f"{stock.name}: ₹{stock.price}")

class Portfolio:
    def __init__(self):
        self.cash = 10000.0
        self.holdings = {}  

    def buy(self, stock, quantity, price):
        cost = quantity * price
        if self.cash >= cost:
            self.cash -= cost
            self.holdings[stock] = self.holdings.get(stock, 0) + quantity
            print(f"Bought {quantity} shares of {stock}")
        else:
            print("Not enough cash!")

    def sell(self, stock, quantity, price):
        if self.holdings.get(stock, 0) >= quantity:
            self.holdings[stock] -= quantity
            self.cash += quantity * price
            print(f"Sold {quantity} shares of {stock}")
        else:
            print("Not enough shares!")

    def show_portfolio(self, market):
        print("\nYour Portfolio:")
        print(f"Cash: ₹{self.cash}")
        total_value = self.cash
        for stock, qty in self.holdings.items():
            stock_price = market.stocks[stock].price
            value = qty * stock_price
            total_value += value
            print(f"{stock}: {qty} shares @ ₹{stock_price} = ₹{value}")
        print(f"Total Portfolio Value: ₹{round(total_value, 2)}")

market = Market()
portfolio = Portfolio()

for day in range(1, 6):  
    print(f"\n--- Day {day} ---")
    market.update_prices()
    market.show_prices()
    portfolio.show_portfolio(market)

    action = input("\nEnter action (buy/sell/skip): ").strip().lower()
    if action in ['buy', 'sell']:
        stock_name = input("Stock name (ABC/XYZ/LMN): ").strip().upper()
        if stock_name not in market.stocks:
            print("Invalid stock.")
            continue
        try:
            qty = int(input("Quantity: "))
        except ValueError:
            print("Invalid quantity.")
            continue
        price = market.stocks[stock_name].price
        if action == 'buy':
            portfolio.buy(stock_name, qty, price)
        else:
            portfolio.sell(stock_name, qty, price)
    else:
        print("No action taken.")

print("\n=== Simulation Complete ===")
portfolio.show_portfolio(market)