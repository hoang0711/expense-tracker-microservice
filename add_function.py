
from expense import Expense

csv_file = "expense_data.csv"


def get_expense():
    """
    This function will ask user for the expense and its amount, then it will save that information in a csv file.
    """
    print("Please provide your expense and amount below!")
    expense_name = str(input("Enter the expense name: "))
    expense_amount = float(input("Enter the amount: "))

    # pass user inputs as variables for the Expense class
    user_expense = Expense(name=expense_name, amount=expense_amount)
    # write the expense and its amount in a csv file
    with open(csv_file, "a") as file:
        file.write(f"{user_expense.name}, {user_expense.amount}\n")
    print("Your expense is saved!")

if __name__ == "__main__":
    get_expense()