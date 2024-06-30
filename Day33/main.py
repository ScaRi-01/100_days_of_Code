#ISS-Overhead Notifier Project (Bangalore)
import requests
from datetime import datetime

my_lat = 12.971599
my_long = 77.594566
def correct_time():
    parameters = {'lat': my_lat, 'lng': my_long, 'formatted':0, 'tzid': 'Asia/Kolkata'}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    current_time = datetime.now().hour
    if sunset <= current_time <= sunrise:
        return True

#ISS location
def ISS_location():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_lat = float(data_iss['iss_position']['latitude'])
    iss_long = float(data_iss['iss_position']['longitude'])

    #Check if the ISS is located near our location
    def check_location(my_lat, my_long, iss_lat, iss_long):
        return abs(my_lat - iss_lat) <= 5.0 and abs(my_long - iss_long) <= 5.0

    if check_location(my_lat, my_long, iss_lat, iss_long):
        return True
