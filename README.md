# week4-finance-tracker
Personal Finance Tracker
Project Description
A comprehensive personal finance tracking application that helps users manage their expenses, categorize spending, and generate insightful reports.

Features
Add, edit, and delete expenses with full validation
Categorize expenses (Food, Transport, Entertainment, Bills, etc.)
Save data to JSON file with automatic backups
Load data on startup with error recovery
Generate monthly expense reports
View category-wise spending breakdown
Set and track monthly budgets
Export data to CSV for external analysis
User-friendly menu interface
How to Run
bash Copy
cd week4-finance-tracker
python run.py
Quality Standards Checklist

How it works:
Modular Import: It pulls in specific classes and functions from your modules package.
Initialization: Every time you start the app, it attempts to load your expenses.json file so you don't lose your history.
Main Loop: A standard while True loop keeps the menu active until you explicitly choose to exit.
Entry Point Guard: The if __name__ == "__main__": block ensures the script only runs if executed directly, not if imported elsewhere.

My Expense Tracker: Project Overview & Specs
The goal is to build a solid expense manager that doesn’t just lose data when I close it. I want it modular, easy to use, and smart enough to handle bad user input without crashing.
Key Features to Build:
Persistent Storage: Use JSON for the main database and CSV for easy exports/imports.
Modular Code: Keep logic separated (file handling vs. report generation) so it's easier to debug.
Bulletproof Errors: Wrap file operations in try/except blocks to catch permissions or missing file issues.
Data Integrity: Validate every input (amounts must be numbers, dates must be valid) before saving.
Insights: Generate category breakdowns and monthly summaries with simple text-based charts.
Safety First: Automated backups and a recovery system in case the main data file gets corrupted.
