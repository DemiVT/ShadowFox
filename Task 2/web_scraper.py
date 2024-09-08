import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://example.com'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific data
titles = soup.find_all('h1')  # Example: extracting all h1 titles

for title in titles:
    print(title.get_text())
