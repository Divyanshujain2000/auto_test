import math

def start_calc(yaw,lat1,lon1):
    
    global lon2
    global lat2
    global bearing
    global distance
    dlon = lon2 - lon1
    y = math.sin(dlon) * math.cos(lat2)
    x = (math.cos(lat1) * math.sin(lat2))-(math.sin(lat1) * math.cos(lat2) * math.cos(dlon))
    bearing = math.atan2(y,x)*rtd
    bearing = bearing - yaw
    distance = math.sqrt(((lat2-lat1)*(lat2-lat1))+((lon2-lon1)*(lon2-lon1)))
    print("bearing="+str(bearing))
    print("distance="+str(distance))