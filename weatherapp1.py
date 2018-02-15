from requests import get
import webbrowser
import folium
import os
import html
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'
station_data = get(url).json()
temps = []
tmax = 0.0
tmin = 100.0
lons = [data['weather_stn_long'] for data in station_data['items']]
lats = [data['weather_stn_lat'] for data in station_data['items']]
wsnames = [html.escape(station['weather_stn_name']) for station in station_data['items']]
for data in station_data['items']:
      if 'ambient_temp' in data:   
          t = data['ambient_temp']
          temps.append(str(t))
map_ws = folium.Map(location=[0, 0], zoom_start=2)
for n in range(len(lons)-1):
    folium.CircleMarker([lats[n], lons[n]],
                        radius = 5,
                        popup = wsnames[n]+':'+temps[n],
                        fill_color = 255).add_to(map_ws)

CWD = os.getcwd()
map_ws.save('index.html')

