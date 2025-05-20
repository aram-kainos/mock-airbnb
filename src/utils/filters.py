def filter_by_price(listings, max_price):
    return [listing for listing in listings if listing.get('price', 0) <= max_price]