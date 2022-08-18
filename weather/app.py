import requests
from flask import Flask, render_template, redirect, session
app=Flask(__name__)

api_key='6b4908b8ab6fb4da0b7881624320662f'

input = input('Enter city:')




@app.route('/')
def index():
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={input}&appid={api_key}')
    weather = weather_data.json()['weather'][0]['description']
    temp = weather_data.json()['main']['temp']
    f_temp=round((temp - 273.15) * (9/5) +32)
    return render_template('display.html', weather=weather, f_temp=f_temp)




if __name__=="__main__":
    app.run(debug=True) 