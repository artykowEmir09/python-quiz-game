import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")

    description = input("Description: ")

    while True:
        try:
            amount = float(input("Amount (RM): "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break
        except ValueError:
            print("Please enter a valid number.")

    category = input("Category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['description']} | "
            f"RM {expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total: RM {total:.2f}")


def category_summary(expenses):
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    for category, amount in categories.items():
        print(f"{category}: RM {amount:.2f}")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    view_expenses(expenses)

    while True:
        try:
            number = int(input("\nEnter expense number to delete: "))

            if 1 <= number <= len(expenses):
                deleted = expenses.pop(number - 1)
                save_expenses(expenses)

                print(
                    f"Deleted: {deleted['description']} "
                    f"(RM {deleted['amount']:.2f})"
                )
                break

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")


def search_expenses(expenses):
    print("\n--- Search Expenses ---")

    keyword = input("Enter keyword: ").lower()

    results = []

    for expense in expenses:
        if (
            keyword in expense["description"].lower()
            or keyword in expense["category"].lower()
        ):
            results.append(expense)

    if not results:
        print("No matching expenses found.")
        return

    for i, expense in enumerate(results, start=1):
        print(
            f"{i}. {expense['description']} | "
            f"RM {expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 35)
        print("       EXPENSE TRACKER")
        print("=" * 35)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Search Expenses")
        print("6. Delete Expense")
        print("7. Exit")
        print("=" * 35)

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            search_expenses(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()