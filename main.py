
import os
import csv
import requests
import json
import time
csv_file = "expense_data.csv"


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
        print("2. Edit an expense")
        print("3. Delete an expense")
        print("4. View all expenses")
        print("5. Show expenses in JSON format")
        print("6. Exit")

        option = input("Pick an option: ")

        if option == "1":
            os.system(f"python add_function.py")

        elif option == "6":
            clear_screen()
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

        elif option == "5":
            clear_screen()
            parser_data = call_csv_parser(parser_request)
            if parser_data["action"] == "done":
                print("Expense data has been converted from CSV format to JSON format successfully!")
                print(parser_data["data"])

        elif option == "2":
            os.system(f"python edit_function.py")

        elif option == "4":
            clear_screen()
            view_expenses()

        elif option == "3":
            os.system(f"python delete_function.py")

        else:
            print("Invalid entry. Please pick again!")


def clear_screen():
    """
    This method will instantly clear the screen.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def view_expenses():
    with open(csv_file, "r") as file:
        csv_read = csv.reader(file)
        expense_list = list(csv_read)

        print("\nThis is the full list of expenses:")
        for line in expense_list:
            print(": ".join(line))


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

if __name__ == "__main__":
    main()