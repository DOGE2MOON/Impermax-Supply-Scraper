# Impermax-Supply-Scraper

An extremely slow and inefficient scraper that returns a dataframe of Impermax data: Supply APR, Borrow APR, and user Supply positions from any and all Impermax deployment via web3 calls to avoid common pitfalls found with frontend scrapers. Contains logic to ignore uninitialized pairs and pairs with a total supply of 0 tokens, otherwise returns 0 to the dataframe. Prints current position to the console due to the long runtime (each pair takes approximately 9 seconds). Updated to include 'speedrun' method, which reduces runtime by ~25%. Can easily be exported to CSV or forked to include Impermax forks.

# Example Usage: 
get_info('Polygon', recipient, False) -> gather all data directly from the chain
get_info('Ethereum', recipient, True) -> use precompiled CSV, gather yield and position data from the chain

# Example Usage (to CSV):
get_info('Polygon', recipient, True).to_csv('filename.csv', encoding='utf-8')
