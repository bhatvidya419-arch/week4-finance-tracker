import json
import os

BUDGET_FILE = 'budget_config.json'

def set_budget(category, amount):
    """Saves a spending limit for a specific category."""
    budgets = load_budgets()
    budgets[category] = float(amount)
    with open(BUDGET_FILE, 'w') as f:
        json.dump(budgets, f)

def load_budgets():
    if not os.path.exists(BUDGET_FILE):
        return {}
    with open(BUDGET_FILE, 'r') as f:
        return json.load(f)

def check_budget_status(current_spending):
    """Compares current totals against set limits."""
    budgets = load_budgets()
    status_report = "\n--- ⚠️ Budget Alerts ---\n"
    for cat, limit in budgets.items():
        spent = current_spending.get(cat, 0)
        if spent > limit:
            status_report += f"OVER BUDGET: {cat} (Spent: ${spent:.2f} | Limit: ${limit:.2f})\n"
        else:
            remaining = limit - spent
            status_report += f"Safe: {cat} (${remaining:.2f} left)\n"
    return status_report

def predict_next_month(expenses):
    """Simple prediction: averages previous spending to estimate next month."""
    if not expenses: return 0
    total = sum(e.amount for e in expenses)
    # Basic logic: total spent / number of entries * average entries per month
    return total / len(expenses) * 10 # Rough estimation factor
