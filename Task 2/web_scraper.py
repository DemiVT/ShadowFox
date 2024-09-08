import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url, output_file):
    try:
        # Send HTTP request
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract titles
        titles = soup.find_all('h1')  # Adjust as needed
        
        # Save data to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title'])
            for title in titles:
                writer.writerow([title.get_text()])
        
        print(f"Data has been scraped and saved to {output_file}")
        
    except requests.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    url = 'https://shadowfox.example.com'  # Replace with the ShadowFox URL
    output_file = 'scraped_data.csv'
    scrape_data(url, output_file)
