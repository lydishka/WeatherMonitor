import requests


def get_weather(city, api_key):
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="
                        f"{api_key}&units=metric&lang=ru").json()
    print(data)
    return data


def get_weather_five_days(city, api_key):
    data = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid="
                        f"{api_key}&units=metric&lang=ru").json()
    print(data)
    return data


def get_feels_like(data):
    return data["main"]["feels_like"]


def get_wind(data):
    return data["wind"]["speed"]


def get_visibility(data):
    return data["visibility"]


def get_name(data):
    return data["name"]


def get_humidity(data):
    return data["main"]["humidity"]


def get_pressure(data):
    pressure = data["main"]["pressure"] * 0.75 # перевод в мм
    return pressure


def get_temp(data):
    return data["main"]["temp"]


def get_desc(data):
    return data["weather"][0]["description"]


def get_weather_icon_url(self, icon_code):
    """Получение URL иконки погоды"""
    return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"



data = get_weather_five_days(city="Москва", api_key="2267c1b6f4893ab4e10c6cd8f2cc84db")
print(data["list"][39]["weather"][0]["description"])
