import requests


def get_weather(city, api_key):
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="
                        f"{api_key}&units=metric&lang=ru").json()
    return data


def get_weather_five_days(city, api_key):
    data = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid="
                        f"{api_key}&units=metric&lang=ru").json()

    weather_temp = list()
    weather_dt = list()
    weather_dates = list()
    weather_dates.append(data["list"][0]["dt_txt"][:10])

    weather_data = dict()
    weather_data[F"temp"] = []
    weather_data[F"dt"] = []


    weather_first_dt = data['list'][0]['dt_txt']

    for i in range(0, 40):
        if weather_first_dt[:10] != data["list"][i]["dt_txt"][:10]:
            weather_dates.append(data["list"][i]["dt_txt"][:10])

            weather_data[F"temp"] += [weather_temp]
            weather_data[F"dt"] += [weather_dt]
            weather_temp = list()
            weather_dt = list()
            weather_first_dt = data['list'][i]["dt_txt"]

        weather_temp.append(data["list"][i]["main"]["temp"])
        weather_dt.append(data["list"][i]["dt_txt"])

    return weather_data, weather_dates[:-1]


def get_feels_like(data):
    feels_like = data["main"]["feels_like"]
    return feels_like


def get_wind(data):
    wind = data["wind"]["speed"]
    return wind


def get_visibility(data):
    visibility = data["visibility"]
    return visibility


def get_name(data):
    name = data["name"]
    return name


def get_humidity(data):
    humidity = data["main"]["humidity"]
    return humidity


def get_pressure(data):
    pressure = data["main"]["pressure"] * 0.75 # перевод в мм
    return pressure


def get_temp(data):
    temp = data["main"]["temp"]
    return temp


def get_desc(data):
    desc = data["weather"][0]["description"]
    return desc


def get_smile(data):
    desc = get_desc(data)
    if "облачность" in desc or "облачно" in desc or "облака" in desc:
        return "⛅"
    elif "пасмурно" in desc:
        return "☁️"
    elif "дождь" in desc or "ливень" in desc:
        return "🌧️"
    elif "морось" in desc or "моросящий" in desc:
        return "🌦️"
    elif "гроза" in desc:
        return "⛈️"
    elif "снег" in desc or "снегопад" in desc:
        return "🌨️"
    else:
        return "☀️"