import json
from src.utils.filters import filter_by_price

def load_listings(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def main():
    listings = load_listings('data/listings.json')
    affordable = filter_by_price(listings, max_price=150)
    print(f"Found {len(affordable)} affordable listings.")

if __name__ == "__main__":
    main()