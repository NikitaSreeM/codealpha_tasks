def stock_tracker():
    stock_prices = {
        "REDBULL": 300,
        "MCLAREN": 250,
        "FERRARI": 400,
        "MERCEDES": 350
    }

    total_investment = 0

    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock name (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock in stock_prices:
            quantity = int(input(f"Enter quantity of {stock}: "))
            total_investment += stock_prices[stock] * quantity
        else:
            print("Stock not found. Please enter a valid stock name.")

    print(f"\nTotal investment value: ${total_investment}")

    # Optional: Save to file
    with open("portfolio_summary.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}\n")

stock_tracker()