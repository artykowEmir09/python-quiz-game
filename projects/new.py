expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    print("\n===== Expenses =====")

    total = 0

    for expense in expenses:
        print(f"{expense['name']}: RM{expense['amount']:.2f}")
        total += expense["amount"]

    print("--------------------")
    print(f"Total: RM{total:.2f}")


while True:
