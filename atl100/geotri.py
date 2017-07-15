### basic geo triagulation module
##
##  based on gaak99 untapped sl4a script circa 2012

import math, sys

def distance(location1, location2):
    "Calc the distance between two GPS loctions"
    R = 6371
    latitude1 = math.radians(location1['latitude'])
    latitude2 = math.radians(location2['latitude'])
    longitude1 = math.radians(location1['longitude'])
    longitude2 = math.radians(location2['longitude'])
    distance = math.acos(math.sin(latitude1) * math.sin(latitude2) + \
			 math.cos(latitude1) * math.cos(latitude2) *\
			 math.cos(longitude2-longitude1)) * R
    return distance
