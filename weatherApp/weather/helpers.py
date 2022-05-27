from datetime import datetime, timedelta


def parseWeather(dic):
    #    "location_name": "Bogota, CO",
    #   "temperature": "17 °C",
    #   "wind": Gentle breeze, 3.6 m/s, west-northwest",
    #   "cloudiness": "Scattered clouds",
    #   "pressure": "1027 hpa",
    #   "humidity": "63%",
    #   "sunrise": "06:07",
    #   "sunset": "18:00",
    #   "geo_coordinates": "[4.61, -74.08]",
    #   "requested_time": "2018-01-09 11:57:00"
    #   "forecast": {...}

    weather = {
        'icon': dic['weather'][0]['icon'],
        'locationName': dic['name'] + ', ' + dic['sys']['country'],
        'temperature': int(dic['main']['temp']),
        'temperatureC': toCelsius(int(dic['main']['temp'])),
        'windSpeed': dic['wind']['speed'],
        'windDirection': degToCompass(dic['wind']['deg']),
        'description': dic['weather'][0]['description'],
        'pressure': dic['main']['pressure'],
        'humidity': dic['main']['humidity'],
        'sunrise': parseTime(dic['sys']['sunrise'], dic['timezone']),
        'sunset': parseTime(dic['sys']['sunset'], dic['timezone']),
        'geoCoordinates': [dic['coord']['lon'], dic['coord']['lat']],
        'requestedTime': datetime.now().strftime("%H:%M:%S")}
    return weather


def toCelsius(temp):
    temperatureC = int((temp - 32) * 5/9)
    return temperatureC


def parseTime(time, timezone):
    timeParsed = datetime.fromtimestamp(time) + timedelta(hours=timezone/3600)
    return timeParsed.strftime('%H:%M:%S')


def degToCompass(num):
    val = int((num/22.5)+.5)
    arr = ["North", "North -> NorthEasth", "North -> East", "East -> NorthEast", "East", "East -> SouthEast", "SouthEast", "South -> SoutEasth",
           "South", "South -> SouthWest", "SouthWest", "West -> SouthWest", "West", "West -> NorthWest", "NorthWest", "North -> NorthWest"]
    return arr[(val % 16)]
