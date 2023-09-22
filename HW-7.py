import requests
from bs4 import BeautifulSoup
import pprint


def get_weather_data(city):
    api_key = "0fe3ef42aed9ab00fb0b17534114b08f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        
        if response.status_code == 200 :
            data = response.json()
            temperature= data["main"]["temp"]
            
            return f'temperature city {city} : {temperature}'
        else :
            return f'city {city} not find'

    except KeyError as e:
        print(f"Error {e}")
    except Exception as e:
        print(f"an error occurred: {e}") 


# london
input_city = input('Enter name city : ')
result = get_weather_data(input_city)
print(result)