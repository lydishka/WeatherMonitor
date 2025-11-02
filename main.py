import requests

def get_weather(city, api_key):
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru").json()

    print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")

get_weather(city="Мурино", api_key="2267c1b6f4893ab4e10c6cd8f2cc84db")
