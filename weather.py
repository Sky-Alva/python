import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timezone

api= '9be09848615ae7175d6530db93731622'

city = 'Medan'#str(input('Enter City Name: '))

geolocator = Nominatim(user_agent = 'test')
location = geolocator.geocode(city)
url = f'https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api}'
response = requests.get(url)

if response.status_code==200: #200 means success
    data = response.json()
    
    print(f"""City Name: {city}
Weather: {data['weather'][0]['description']}
Temperature: {(data['main']['temp']-273)//1} °C
Pressure: {data['main']['pressure']} hPa
Humidity: {data['main']['humidity']} %
Wind: {data['wind']['speed']} m/s on {data['wind']['deg']}°
Local Time: {datetime.fromtimestamp(int(datetime.timestamp(datetime.utcnow()))+data['timezone'])}
Last Updated Time (on your time): {datetime.fromtimestamp(data['dt'])}""")

else: 
    print(f'Error When Fetching Data, it may be because there is no city with such name ({city}) or server issue')