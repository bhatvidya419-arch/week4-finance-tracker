from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        # We validate during initialization to ensure data integrity
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = category
        self.description = description

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

    @staticmethod
    def validate_amount(amount):
        try:
            val = float(amount)
            if val <= 0:
                raise ValueError
            return val
        except ValueError as e:
            raise ValueError("Amount must be a positive number.") from e

    def to_dict(self):
        """Converts the object to a dictionary for JSON storage."""
        return vars(self)
