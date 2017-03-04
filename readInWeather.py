import netCDF4 as nc4
import pylab as pl
import math
import pandas as pd
import datetime


year = -9999
root_grp = None


def getMeteoValue(meteoVar,time, latitude, longitude):
    global year
    global root_grp
    currentYear = pd.Timestamp(time).year
    #print(currentYear)
    if (currentYear != year):
        year = currentYear
        print 'data/d3_'+str(year)+'.nc'
        root_grp = nc4.Dataset('data/d3_'+str(year)+'.nc')
    meteoVariable = root_grp.variables[meteoVar]

    #print meteoVariable.dimensions
    latVar = root_grp.variables['latitude']
    lonVar = root_grp.variables['longitude']
    totalLats = len(latVar)
    totalLons = len(lonVar)
    maxLat = max(latVar)
    maxLon = max(lonVar)
    minLat = min(latVar)
    minLon = min(lonVar)
    cellSizeLat = (max(latVar) - min (latVar))/totalLats
    cellSizeLon = (max(lonVar) - min(lonVar)) / totalLons
    cellTileLat = math.ceil((-min(latVar) + latitude)/cellSizeLat)
    cellTileLon = math.ceil((-min(lonVar) + longitude)/cellSizeLon)

    time_var = root_grp.variables['time']

    #dtime = nc4.num2date(time_var[:], time_var.units)

    #prova = time_var.sel(time = time)

    test = nc4.date2index(pd.Timestamp(time), time_var,  select= "nearest")


    #print("hello")

    #print precipitation[test,cellTileLat,cellTileLon]

    return meteoVariable[test,cellTileLat,cellTileLon]

#print(len(temp))
#print(temp[0])

#hs = pd.Series(root_grp.variables['area'].dimensions['lat'])




#getMeteoValue(datetime.datetime.strptime("2015-01-04 10:00", "%Y-%m-%d %H:%M"),52,6)