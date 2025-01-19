import requests
from bs4 import BeautifulSoup

# URL alvo
url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Exemplo: Extrair títulos (h1)
titles = soup.find_all("h1")
for title in titles:
    print(title.get_text())