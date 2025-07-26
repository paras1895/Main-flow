
import csv
import os

DATA_FILE = "budget_data.csv"

def load_data():
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                data.append(row)
    return data

def save_data(data):
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["type", "category", "amount"])
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def add_entry(data):
    try:
        t = input("Type (income/expense): ").strip().lower()
        if t not in ['income', 'expense']:
            raise ValueError("Invalid type. Must be 'income' or 'expense'.")
        category = input("Category: ").strip().capitalize()
        amount = float(input("Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        data.append({"type": t, "category": category, "amount": amount})
        print("Entry added.")
    except ValueError as e:
        print(f"Error: {e}")

def summarize(data):
    income_total = sum(e['amount'] for e in data if e['type'] == 'income')
    expense_total = sum(e['amount'] for e in data if e['type'] == 'expense')
    balance = income_total - expense_total

    print("\n=== Summary ===")
    print(f"Total Income : ${income_total:.2f}")
    print(f"Total Expense: ${expense_total:.2f}")
    print(f"Balance      : ${balance:.2f}")

    category_summary = {}
    for e in data:
        if e['type'] == 'expense':
            category_summary[e['category']] = category_summary.get(e['category'], 0) + e['amount']

    if category_summary:
        print("\n--- Expense Breakdown ---")
        for cat, amt in category_summary.items():
            percent = (amt / expense_total) * 100 if expense_total else 0
            print(f"{cat}: ${amt:.2f} ({percent:.1f}%)")

def suggest_savings(data):
    print("\n=== Budget Suggestions ===")
    expense_data = [e for e in data if e['type'] == 'expense']
    if not expense_data:
        print("No expenses recorded. Keep tracking!")
        return

    category_totals = {}
    for e in expense_data:
        category_totals[e['category']] = category_totals.get(e['category'], 0) + e['amount']

    sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    top_cat, top_amt = sorted_cats[0]
    print(f"You're spending the most on '{top_cat}' (${top_amt:.2f}).")
    print("Consider reducing spending in this category.")

    if top_amt > 200:
        print("Try setting a monthly limit or switching to cheaper alternatives.")

    total_expense = sum(category_totals.values())
    if total_expense > 0:
        avg_spending = total_expense / len(category_totals)
        high_spenders = [cat for cat, amt in category_totals.items() if amt > avg_spending * 1.5]
        if high_spenders:
            print("\nYou are overspending in:")
            for cat in high_spenders:
                print(f" - {cat}")
            print("Try cutting back 10-20% in these areas.")

def show_menu():
    print("\n--- Personal Budget Advisor ---")
    print("1. Add Entry")
    print("2. View Summary")
    print("3. Get Saving Suggestions")
    print("4. Save & Exit")

def main():
    data = load_data()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_entry(data)
        elif choice == '2':
            summarize(data)
        elif choice == '3':
            suggest_savings(data)
        elif choice == '4':
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number 1-4.")

if __name__ == "__main__":
    main()
