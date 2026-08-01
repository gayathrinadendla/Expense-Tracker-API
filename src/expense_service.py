import json,os
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
def load_expenses():
    with open(DATA_FILE,"r")as file:
        return json.load(file)
def save_expenses(expenses):
    with open(DATA_FILE,"w")as file:
        json.dump(expenses,file,indent=4)
def add_expense(data):
    expenses=load_expenses()
    new_expense={
        "id":len(expenses)+1,
        "title":data.get("title"),
        "amount":data.get("amount"),
        "category":data.get("category"),
        "date":data.get("date")
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense
def get_all_expenses():
    expenses = load_expenses()
    return expenses
def filter_by_category(category):
    expenses = load_expenses()
    filtered = []
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            filtered.append(expense)
    return filtered
def calculate_total():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return {"total": total}
def delete_expense(expense_id):
    expenses = load_expenses()
    updated = []
    deleted = False
    for expense in expenses:
        if expense["id"] != expense_id:
            updated.append(expense)
        else:
            deleted = True
    if deleted:
        save_expenses(updated)
    return deleted