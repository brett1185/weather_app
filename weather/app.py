import requests

api_key='6b4908b8ab6fb4da0b7881624320662f'

input = input('Enter city:')

weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={input}&appid={api_key}')

weather = weather_data.json()['weather'][0]['description']
temp = weather_data.json()['main']['temp']
f_temp=round((temp - 273.15) * (9/5) +32)

print(weather, f_temp)