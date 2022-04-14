import pandas as pd
from mapbox import Directions
from mapbox import Geocoder

def geocode(name):
    '''https://mapbox-mapbox.readthedocs-hosted.com/en/latest/geocoding.html'''
    geocoder = Geocoder()
    coords = geocoder.forward(name).geojson()['features'][0]
    return [int(coord) for coord in coords['geometry']['coordinates']]

def formatLocation(name, latitude, longitude):
'''
mapbox supports inputs in the form of iterables of GeoJSON-like Features
>>> origin = {
...    'type': 'Feature',
...    'properties': {'name': 'Portland, OR'},
...    'geometry': {
...        'type': 'Point',
...        'coordinates': [-122.7282, 45.5801]}}
>>> destination = {
...    'type': 'Feature',
...    'properties': {'name': 'Bend, OR'},
...    'geometry': {
...        'type': 'Point',
...        'coordinates': [-121.3153, 44.0582]}}
'''
    pass

def assignLocations(drivers, locations):
    # naive alg:
    # 1. assign a random location to each of the drivers
    # 2. loop through each driver (random order again) and add the location that is nearest to the driver
    pass

def findOptimalRoute(driversAndLocation):
    # traveling salesman problem
    pass

def calculateCost(driversAndLocation):
    # calculate the time it takes each driver to go to their locations based on the optimal route
    # if any cost exceeds the time required to deliver all food, rerun assignLocations (the entire alg)
    # if after 10 tries, there still isn't an optimal route, then we will manually make edits to the best plan the alg gives us
    pass

if __name__ == "__main__":
    # must import number of drivers and a list of all the locations
    # assignLocations(drivers, locations)
    pass
