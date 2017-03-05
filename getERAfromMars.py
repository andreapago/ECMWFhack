#!/usr/bin/env python
#
#Get ERAinterim datas from MARS webapi
#
# usage: python getERAfromMARS.py startyear [endyear]
#
from ecmwfapi import ECMWFDataServer
import sys
server = ECMWFDataServer()

startyear=int(sys.argv[1])
endyear=startyear
if (len(sys.argv)>2) :
  endyear=int(sys.argv[2])

for year in range(startyear, endyear+1):
  print >>sys.stderr, year

  server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "%s-01-01/to/%s-12-31"%(year,year),
    "expver": "1",
    "grid": "0.125/0.125",
    "area": "54/3.5/50/7.5",
    "levtype": "sfc",
    "param": "49.128/144.128/165.128/166.128/167.128/168.128/228.128",
    "step": "3/6/9/12",
    "stream": "oper",
    "time": "00:00:00/12:00:00",
    "type": "fc",
    "format": "netcdf",
    "target": "d3_%04d.nc"%year,
  })
