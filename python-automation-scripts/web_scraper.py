import requests
from bs4 import BeautifulSoup

def get_title(url):
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.title.string if soup.title else ""

if __name__ == "__main__":
    url = input("URL: ").strip() or "https://example.com"
    print(get_title(url))