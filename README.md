# Expense Tracker

A simple application that can help users keep track of their daily expenses and manage their spendings. The app consists of 
a Main program (UI) and several microservices.

## Language:
Python

## How to use the Main program to REQUEST and RECEIVE data from the quote_generator microservice:
1. Create a function within the main program to make a call request to the microservice.
2. Depending on the programming language, install and import the necessary module for GET/POST methods (e.g. import requests module for Python language).
3. Since quote_generator will display the quote on the localhost, make sure to list that localhost (with port #) as the url for the GET method.
4. The current port # for quote_generator is 5025. If this port is modified, make sure to update it in the main function's localhost url, also.
5. Perform a GET method on the localhost url.
6. Return the fetched data in the JSON format and print it.

Example call in Python:
```bash
import requests

def display_random_quote():
  url = "http://localhost:5025/fetch-quote"
  response = requests.get(url)
  return response.json()

print(display_random_quote())
```
UML Diagram:

![Quote Generator UML](https://github.com/user-attachments/assets/77ddcc93-8f6f-468f-ab0a-3a133a5209c4)
