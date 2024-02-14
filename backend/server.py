from flask import Flask, render_template, request
from flask_cors import CORS
import weather_funcs
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/weather/current')
def get_temp():
    day = int(request.args.get('day'))
    # Returning an api for showing in  reactjs
    data = {
        'day': f"{weather_funcs.return_days(when=day)[0][0]}",
        'temp': f"{weather_funcs.return_days(when=day)[0][1]}",
        'condition': f"{weather_funcs.return_days(when=day)[0][2]}",
        'date': f"{weather_funcs.return_days(when=day)[0][3]}"
        }
    return data

@app.route('/weather/all')
def get_all_weather():
    return weather_funcs.return_days(asJson=True)

@app.route('/weather/infos/all')
def get_all_infos():
    return weather_funcs.get_all_infos()

@app.errorhandler(404)
def not_found(e):
    return "404 Error: Ressource not found!"

# print(weather_funcs.return_days(when=0)[0][2])
app.run(debug=True)
# app.run(debug=False, host="localhost", port=8080)