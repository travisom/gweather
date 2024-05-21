from flask import Flask, render_template, request
import requests
from datetime import datetime
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def search():
    api_key = "2e55387f2ae53ea3f1b86cf7da9d81d9"
    city = "Adelaide"
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&APPID=" + api_key
    url2 = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + api_key
    print(url)
    print(url2)
    response = requests.get(url).json()
    print(response)
    city_name = response["city"]["name"]
    city_population = response["city"]["population"]
    print(city_name)
    print(city_population)

    # Forecast api data consumption
    forecast_list = response['list']
    forecast_data = []
    index = 0
    while index < len(forecast_list):
        dt_txt = forecast_list[index]['dt_txt']
        temp = forecast_list[index]['main']['temp'] - 273
        icon = forecast_list[index]['weather'][0]['icon']
        description = forecast_list[index]['weather'][0]['description']
        # Convert the string to a datetime object
        date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        # You can also get the day name
        day_name = date_object.strftime('%A')
        print(day_name)
        dict = {
            "dt_txt": dt_txt,
            "temp": int(temp),
            "icon_url": "http://openweathermap.org/img/w/" + icon + ".png",
            "description": description,
            "day_of_week": day_name

        }
        forecast_data.append(dict)
        index += 8
    print(forecast_data)

    # Current weather (url2) api data consumption
    #icon, max temp, humidity, precipitation and wind
    response = requests.get(url2).json()


    return render_template('home.html',forecast_data=forecast_data)






if __name__ == '__main__':
    app.run(debug=True, port=5002)

