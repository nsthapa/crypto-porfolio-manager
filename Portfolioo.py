print("=== Crypto Portfolio Manager ===")

portfolio = []


def find_coin(name):
    for coin in portfolio:
        if coin["name"].lower() == name.lower():
            return coin
    return None


def add_crypto():
    name = input("Enter crypto name: ").strip()

    if not name:
        print("Crypto name can't be empty.\n")
        return

    try:
        amount = float(input("Enter amount owned: "))
        price = float(input("Enter current price (USD): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        return

    if amount < 0 or price < 0:
        print("Amount and price must be positive numbers.\n")
        return

    existing = find_coin(name)
    if existing:
        existing["amount"] += amount
        existing["price"] = price
        existing["value"] = existing["amount"] * existing["price"]
        print(f"{name} updated. New amount: {existing['amount']}\n")
        return

    portfolio.append({
        "name": name,
        "amount": amount,
        "price": price,
        "value": amount * price
    })

    print(f"{name} added successfully!\n")


def remove_crypto():
    if not portfolio:
        print("Portfolio is empty.\n")
        return

    name = input("Enter crypto name to remove: ").strip()
    coin = find_coin(name)

    if not coin:
        print(f"{name} not found in portfolio.\n")
        return

    portfolio.remove(coin)
    print(f"{name} removed.\n")


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
        total_value += coin["value"]

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
            total_value += coin["value"]

        file.write("-" * 40 + "\n")
        file.write(f"Total Portfolio Value: ${total_value:.2f}\n")

    print("Portfolio saved to portfolio_summary.txt\n")


def main():
    while True:
        print("1. Add Crypto")
        print("2. Remove Crypto")
        print("3. View Portfolio")
        print("4. Save Portfolio")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_crypto()
        elif choice == "2":
            remove_crypto()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.\n")


if __name__ == "__main__":
    main()
