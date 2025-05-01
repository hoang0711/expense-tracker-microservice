import csv

csv_file = "expense_data.csv"

def edit_expense(current_expense, new_expense, new_amount):
    """
    This function takes as parameters the current expense, new expense and new amount. It will ask the user which
    current expense needs to be edited, and prompts them to enter the new expense and amount. The new expense and
    amount will be saved in the csv file.
    """
    # initiate an empty list for the new expense and amount data
    updated_line = []
    expense_matched = False

    with open(csv_file, "r", newline="") as file:
        csv_read = csv.reader(file)

        # loops through each line, if the expense name matches the name that the user wishes to edit, replace that
        # expense and amount with the new expense and new amount
        for line in csv_read:
            if line[0] == current_expense and not expense_matched:
                line[0] = new_expense
                line[1] = new_amount
                expense_matched = True
            updated_line.append(line)

    # write the new expense and amount in the csv file
    if expense_matched:
        with open(csv_file, "w", newline="") as file:
            csv_write = csv.writer(file)
            csv_write.writerows(updated_line)
        print("Expense was edited and updated successfully!")
    else:
        print("The expense you've entered doesn't exist. Please enter again!")


if __name__ == "__main__":
    current_expense = input("Enter the expense you wish to edit: ")
    new_expense = input("Enter the new expense name: ")
    new_amount = input("Enter the new amount: ")
    edit_expense(current_expense, new_expense, new_amount)
