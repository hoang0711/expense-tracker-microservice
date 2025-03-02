from expense import Expense
import os
import csv
import requests
import json
import time

def main():
    """
    The main program that displays the Menu with options for the UI. It will call on other methods depending on
    which option the user will choose.
    """
    clear_screen()

    print(f"WELCOME TO YOUR PERSONAL EXPENSE TRACKER!\n"
          f"This application can keep track of your daily expenses and help you manage your spending habits.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Exit")
        print("3. Display an inspirational quote")
        print("4. Show expenses in JSON format")

        option = input("Pick an option: ")

        if option == "1":
            clear_screen()    # After pick option 1, the screen will clear to start a new page before get_expense() starts
            get_expense()

        elif option == "2":
            while True:
                confirm_exit = input("\nThis option will close the Expense Tracker entirely and you will have to run the program again to manage your expenses. "
                                     "\nDo you want to exit? (y/n): ").lower()

                if confirm_exit == "y":
                    print("\nExiting Expense Tracker program.\n"
                            "GOODBYE!")
                    quit()

                elif confirm_exit == "n":
                    main()
                    continue
                else:
                    print("Invalid entry. Please try again!")

        elif option == "3":
            print(generate_quote())

        elif option == "4":
            parser_data = call_csv_parser(parser_request)
            if parser_data["action"] == "done":
                print("Expense data has been converted from CSV format to JSON format successfully!")
                print(parser_data["data"])

        else:
            print("Invalid entry. Please pick again!")

    # Get user expense
    #expense = get_expense()
    #print(expense)

    # Save expense to a file
    #save_expense(expense, your_saved_expenses)

    # Show a list of expenses
    show_expense_list(your_saved_expenses)

def clear_screen():
    """
    This method will instantly clear the screen.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')





def generate_quote():
    """
    This function makes a call to the quote_generator microservice so it can fetch a random quote from
    an external API and display in the UI.
    """
    # define the local host url to make a 'get' request with quote_generator.py
    quote_url = "http://localhost:5025/fetch-quote"

    response = requests.get(quote_url)
    if response.status_code == 200:
        return f'"{response.json()}"'
    else:
        return 'Connection error!'


def call_csv_parser(request):
    with open("csv_service.json", "w") as file:
        json.dump(request, file, indent=3)
    time.sleep(2)
    with open("csv_service.json", "r") as file:
        request = json.load(file)
    return request

parser_request = {
    "action": "run",
    "csv_file_path": r"C:\Users\hoang\Documents\CS361assignments\expense tracker\expense_data.csv",
    "output_format": "json",
    "output_path": r"C:\Users\hoang\Documents\CS361assignments\expense tracker\expense_data.json",
    "data": "",
    "info": ""
}


def get_expense():
    """
    This method will prompt the user to enter an expense and its amount. It will then store them in a CSV file.
    """
    clear_screen()
    print("Please provide your expense and amount below!")
    expense_name = str(input("Enter the expense name: "))
    expense_amount = float(input("Enter the amount: "))
    user_expense = Expense(name=expense_name, amount=expense_amount)
    with open("expense_data.csv", "a") as expensefile:
        expensefile.write(f"{user_expense.name}, {user_expense.amount}\n")
    print("Your expense is saved!")


def show_expense_list(your_saved_expenses):
    expense_list: list[Expense] = []
    with open(your_saved_expenses, "r") as efile:
        lines = efile.readlines()
        for line in lines:
            expense_name, expense_amount = line.strip().split(",")
            #print(expense_name, expense_amount)

            item_per_line = Expense(name=expense_name, amount=float(expense_amount))
            expense_list.append(item_per_line)

    expense_dict = {}
    for expense in expense_list:
        key = expense.name
        if key in expense_dict:
            expense_dict[key] += expense.amount
        else:
            expense_dict[key] = expense.amount

    for key, amount in expense_dict.items():
        print(f"   {key}: ${amount:.2f}")

if __name__ == "__main__":
    main()