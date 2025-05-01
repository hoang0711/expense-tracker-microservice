import csv

csv_file = "expense_data.csv"

def delete_expense(csv_file):
    """
    This function will ask the user to enter the name of the expense they wish to delete. If the entered expense is
    found, it will be removed from the csv file.
    """
    user_input = input("Enter the expense to be deleted: ").strip()
    updated_line = []
    expense_matched = False

    with open(csv_file, "r", newline="") as file:
        csv_read = csv.reader(file)
        header = next(csv_read)
        updated_line.append(header)

        # loops through each line and check if the entered expense matches one of the expense's names in the csv file
        for line in csv_read:
            if line and line[0].strip().lower() == user_input.lower():
                expense_matched = True
            else:
                updated_line.append(line)

    # if the name matches, delete that row of expense and its amount from the csv file
    if expense_matched:
        with open(csv_file, "w", newline="") as file:
            csv_write = csv.writer(file)
            csv_write.writerows(updated_line)
        print("Expense was deleted successfully!")
    else:
        print("The expense cannot be found. Please enter again.")

if __name__ == "__main__":
    delete_expense(csv_file)