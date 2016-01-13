import pandas as pd
import requests
import time

def get_elevation(location):
  url = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
  url = url + str(location[0]) + ',' + str(location[1])

  response = requests.get(url)
  elevation_dict = response.json()

  return elevation_dict['results'][0]['elevation']

stations = pd.read_csv('data/station_data.csv')
#print stations.columns

elevations = []
for loc in zip( stations.lat, stations.long ):
  elev = get_elevation(loc)
  elevations.append( elev )
  time.sleep(10)
  print elev

stations['elevation'] = pd.DataFrame(elevations)
#print stations

stations.to_csv('data/station_elevation_data.csv',index=False)

# test case
#print get_elevation( (38,118) )

