import requests
import time
import os
import pyfiglet
from termcolor import colored
from datetime import datetime

CRYPTO_ID = 'bitcoin'  # ID for Bitcoin
bitcoin_price = "Fetching Price..."  # Default message before the initial price is fetched
previous_price = None  # To store the previous price for comparison
color = "white"  # Initialize color to white
LOG_FILE = '/Users/pinax/Desktop/python/simple_apps/debug_log.txt'  # Path for the debug log


def fetch_bitcoin_price():
    """Fetch the current price of Bitcoin in USD."""
    endpoint = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": CRYPTO_ID,
        "vs_currencies": "usd"
    }
    headers = {"accept": "application/json"}

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()[CRYPTO_ID]['usd']
    else:
        return None


# Function to generate large ASCII representation with color
def print_ascii_price(price, color):
    # Check if price is a string (e.g., "Fetching Price...") or a number
    formatted_price = price if isinstance(price, str) else f"Bitcoin ${price:,.0f}"
    
    # Use pyfiglet to create large text
    ascii_text = pyfiglet.figlet_format(formatted_price)

    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the large ASCII text with color
    if color == 'green':
        print(colored(ascii_text, 'green'))
    elif color == 'red':
        print(colored(ascii_text, 'red'))
    else:
        print(ascii_text)  # Default to white


# Function to write debug logs to file
def log_debug_info(price, color):
    with open(LOG_FILE, "a") as log_file:  # Append to the log file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Price: {price}, Color: {color}\n")


# Main loop: fetch Bitcoin price every 5 seconds, then continuously display it as ASCII
while True:
    # Fetch and update Bitcoin price every 5 seconds
    new_price = fetch_bitcoin_price()
    if new_price:
        # Determine color based on price change
        if previous_price is not None:
            color = "green" if new_price > previous_price else "red" if new_price < previous_price else "white"
        else:
            color = "white"  # Default to white if no previous price
        
        bitcoin_price = new_price  # Update the in-memory variable
        previous_price = new_price  # Store current price for the next comparison

        # Log the new price and color to the debug log
        log_debug_info(bitcoin_price, color)

    # Continuously print the price stored in memory every 1 second
    for _ in range(5):  # Loop 5 times to print every second within the 5-second fetch cycle
        print_ascii_price(bitcoin_price, color)
        time.sleep(1)
