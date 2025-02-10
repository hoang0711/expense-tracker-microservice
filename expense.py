
class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"You've entered: {self.name}, ${self.amount}."