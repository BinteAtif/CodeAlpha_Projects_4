# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 300,
    "AMZN": 3300
}

def main():
    total_investment = 0
    stock_portfolio = {}

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ', '.join(stock_prices.keys()))
    print("Enter 'done' when you are finished.\n")

    while True:
        stock_name = input("Enter stock name: ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not found. Please enter a valid stock name.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Please enter a positive integer for quantity.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        stock_portfolio[stock_name] = stock_portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}.\n")

    # Calculate total investment
    for stock, qty in stock_portfolio.items():
        total_investment += qty * stock_prices[stock]

    print("\nYour Portfolio:")
    for stock, qty in stock_portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional: Save to file
    save_option = input("Would you like to save the result? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter filename (with extension, e.g., portfolio.txt): ")
        try:
            with open(filename, 'w') as file:
                file.write("Stock Portfolio:\n")
                for stock, qty in stock_portfolio.items():
                    file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each\n")
                file.write(f"\nTotal Investment Value: ${total_investment}\n")
            print(f"Results saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()