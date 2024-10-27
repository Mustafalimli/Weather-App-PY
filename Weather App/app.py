from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'fff234e034824c4382b7bc96739de31c'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"message": "Şehir bulunamadı!"}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
