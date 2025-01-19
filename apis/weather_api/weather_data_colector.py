import requests

API_KEY = "sua_chave_api"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Cidade alvo
city = "São Paulo"
url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(url)
data = response.json()

# Exemplo: Exibir temperatura
if data["cod"] == 200:
    temperature = data["main"]["temp"] - 273.15
    print(f"Temperatura em {city}: {temperature:.2f}°C")
else:
    print("Erro ao buscar dados.")