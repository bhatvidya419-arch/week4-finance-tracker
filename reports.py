import statistics

def generate_monthly_summary(expenses):
    """Calculates total spending and average expense per item."""
    if not expenses:
        return "No data to report."
    
    amounts = [e['amount'] for e in expenses]
    total = sum(amounts)
    avg = statistics.mean(amounts)  #
    
    summary = f"--- 📊 Monthly Summary ---\n"
    summary += f"Total Spending: ${total:.2f}\n"
    summary += f"Average Expense: ${avg:.2f}\n"
    summary += f"Number of Entries: {len(expenses)}\n"
    return summary

def get_category_breakdown(expenses):
    """Groups expenses by category and returns a dictionary of totals."""
    breakdown = {}
    for e in expenses:
        cat = e['category']
        breakdown[cat] = breakdown.get(cat, 0) + e['amount']
    return breakdown

def text_bar_chart(data):
    """Generates a simple text-based bar chart for category spending."""
    if not data:
        return "No category data available."
    
    max_val = max(data.values())
    chart = "\n--- 📈 Spending by Category ---\n"
    for label, value in data.items():
        # Scale the bar to a max width of 20 characters
        bar_length = int((value / max_val) * 20) if max_val > 0 else 0
        bar = "█" * bar_length
        chart += f"{label:12} | {bar} ${value:.2f}\n"
    return chart
