#pip install beautifulsoup4
#pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup

# Target URL
url = "http://books.toscrape.com"

# Send a GET request
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book containers
books = soup.find_all('article', class_='product_pod')

# Find all book containers
book_data = []
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}\nPrice: {price}\n")
    book_data.append({"Title": title, "Price": price})
    df = pd.DataFrame(book_data)

    # Optional: Display the DataFrame
    print(df)
