print("=== Crypto Portfolio Manager ===")

portfolio = []

def add_crypto():
    name = input("Enter crypto name: ").strip()

    try:
        amount = float(input("Enter amount owned: "))
        price = float(input("Enter current price (USD): "))

        if amount < 0 or price < 0:
            print("Amount and price must be positive numbers.")
            return

        value = amount * price
        portfolio.append({
            "name": name,
            "amount": amount,
            "price": price,
            "value": value
        })

        print(f"{name} added successfully!\n")

    except ValueError:
        print("Invalid input. Please enter numeric values.\n")


def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.\n")
        return

    total_value = 0
    print("\n--- Portfolio Summary ---")
    print(f"{'Crypto':<15} {'Amount':<10} {'Price(USD)':<12} {'Value(USD)':<12}")
    print("-" * 55)

    for coin in portfolio:
        print(f"{coin['name']:<15} {coin['amount']:<10} {coin['price']:<12} {coin['value']:<12.2f}")
        total_value += coin['value']

    print("-" * 55)
    print(f"{'Total Portfolio Value:':<40} ${total_value:.2f}\n")


def save_to_file():
    if not portfolio:
        print("Nothing to save.\n")
        return

    with open("portfolio_summary.txt", "w") as file:
        total_value = 0
        file.write("Crypto Portfolio Summary\n")
        file.write("-" * 40 + "\n")

        for coin in portfolio:
            file.write(f"{coin['name']} - {coin['amount']} units - ${coin['value']:.2f}\n")
            total_value += coin['value']

        file.write("-" * 40 + "\n")
        file.write(f"Total Portfolio Value: ${total_value:.2f}\n")

    print("Portfolio saved to portfolio_summary.txt\n")


while True:
    print("1. Add Crypto")
    print("2. View Portfolio")
    print("3. Save Portfolio")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_crypto()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        save_to_file()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please select 1-4.\n")
