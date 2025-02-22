
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# use App Routing decorator to bind random_quote() function to /fetch-quote URL path
@app.route('/fetch-quote', methods=['GET'])

def random_quote():
    """
    This function will fetch a random quote from an external API.
    """
    # zenquotes.io will be the external API to fetch random quotes from
    response = requests.get('https://zenquotes.io/api/random')

    if response.status_code == 200:        # code 200 means successful connection
        quote = response.json()
        return jsonify(quote[0]['q'])      # return only the quote section from the data
    else:
        return 'Connection error! Unable to retrieve data!'

def main():
    print((random_quote()))

if __name__ == "__main__":
    app.run(port=5025)                     # run on local host port 5025

