# Impermax-Supply-Scraper

An extremely slow and inefficient scraper that returns a dataframe of Impermax data: Supply APR, Borrow APR, and user Supply positions from any and all Impermax deployment via web3 calls to avoid common pitfalls found with frontend scrapers. Contains logic to ignore uninitialized pairs and pairs with a total supply of 0 tokens in order to actually scrape data, otherwise returns 0 to the dataframe. Prints current position to the console due to the extremely long runtime (each pair takes approximately 9 seconds). Can easily be exported to CSV or forked to include any Impermax forks.

# Example Usage: 
get_info('Polygon', recipient)

(to CSV)
get_info('Polygon', recipient).to_csv('filename.csv', encoding='utf-8')
