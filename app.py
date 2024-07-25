from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '2aecf04cb5f79b16e630804d7dee4490'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key
    response = requests.get(complete_url)
    weather_data = response.json()
    
    # Print the API response for debugging
    print(weather_data)
    
    # Check if the 'main' key exists in the response
    if 'main' in weather_data:
        return render_template('weather.html', weather=weather_data)
    else:
        # Handle the case where the city is not found or other errors
        error_message = weather_data.get('message', 'An error occurred')
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
