import requests
import time
import os
import pyfiglet
from termcolor import colored

# Ask the user to enter the cryptocurrency ticker
CRYPTO_ID = input("Enter the cryptocurrency ticker you want to track (e.g., 'bitcoin', 'ethereum'): ").strip().lower()

bitcoin_price = "Fetching Price..."  # Default message before the initial price is fetched
previous_price = None  # To store the previous price for comparison
color = "white"  # Initialize color to white


def fetch_crypto_price(crypto_id):
    """Fetch the current price of the specified cryptocurrency in USD."""
    endpoint = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }
    headers = {"accept": "application/json"}

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get(crypto_id, {}).get('usd')
    else:
        return None


# Function to generate large ASCII representation with color
def print_ascii_price(price, color):
    # Check if price is a string (e.g., "Fetching Price...") or a number
    formatted_price = price if isinstance(price, str) else f"{CRYPTO_ID.capitalize()} ${price:,.2f}"
    
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


# Main loop: fetch cryptocurrency price every 5 seconds, then continuously display it as ASCII
while True:
    # Fetch and update the cryptocurrency price every 5 seconds
    new_price = fetch_crypto_price(CRYPTO_ID)
    if new_price:
        # Only set the color to green or red after the first price update
        if previous_price is not None:
            if new_price > previous_price:
                color = "green"
            elif new_price < previous_price:
                color = "red"
        else:
            color = "white"  # First time, color will be white

        bitcoin_price = new_price  # Update the in-memory variable
        previous_price = new_price  # Store current price for the next comparison

    # Continuously print the price stored in memory every 1 second
    for _ in range(5):  # Loop 5 times to print every second within the 5-second fetch cycle
        print_ascii_price(bitcoin_price, color)
        time.sleep(1)
