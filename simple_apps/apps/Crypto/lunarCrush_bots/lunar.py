import requests
from config import API_KEY  # Ensure you have a config.py file with your API_KEY

def fetch_all_coins(api_key):
    """
    Fetches cryptocurrencies within specified market cap and AltRank™ ranges (in millions USD for market cap,
    and rank number for AltRank™), and prints their AltRank™, name, symbol, market cap, and last price
    in a formatted and aligned manner with headers.
    
    Parameters:
    - api_key (str): Your LunarCrush API key.
    """
    url = "https://lunarcrush.com/api4/public/coins/list/v2"
    headers = {'Authorization': f'Bearer {api_key}'}

    min_market_cap_millions = float(input("\nEnter minimum market cap (in millions USD): "))
    max_market_cap_millions = float(input("Enter maximum market cap (in millions USD): "))
    min_rank = int(input("Enter minimum AltRank™: "))
    max_rank = int(input("Enter maximum AltRank™: "))
    print()
    print()

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        coins_data = response.json().get('data', [])
        
        filtered_coins = [
            coin for coin in coins_data
            if min_market_cap_millions * 1e6 <= coin.get('market_cap', float('inf')) <= max_market_cap_millions * 1e6
            and min_rank <= coin.get('alt_rank', float('inf')) <= max_rank
        ]
        sorted_coins = sorted(filtered_coins, key=lambda x: x.get('alt_rank', float('inf')))
        
        max_name_length = max(len(f"{coin.get('name')} ({coin.get('symbol')})") for coin in sorted_coins)
        max_market_cap_length = max(len(f"{coin.get('market_cap') / 1e6:.2f}M USD") for coin in sorted_coins)

        # Prepare headers
        rank_header = "Rank"
        token_header = "Token".ljust(max_name_length)
        mcap_header = "mCap".ljust(max_market_cap_length)
        price_header = "$"
        header_line = f"{rank_header} | {token_header} | {mcap_header} | {price_header}"
        separator_line = " " * len("{alt_rank_formatted}{name_symbol}{market_cap}{last_price}")
        
        print(header_line)
        print(separator_line)

        for coin in sorted_coins:
            alt_rank_formatted = str(coin.get('alt_rank')).zfill(4)
            name_symbol = f"{coin.get('name')} ({coin.get('symbol')})".ljust(max_name_length)
            market_cap = f"{coin.get('market_cap') / 1e6:.2f}M USD".ljust(max_market_cap_length)
            last_price = f"{coin.get('price', 0):.4f}"
            print(f"{alt_rank_formatted} | {name_symbol} | {market_cap} | {last_price}")
            
    except requests.RequestException as error:
        print(f"Error fetching data: {error}")

# Example usage
fetch_all_coins(API_KEY)
print()
