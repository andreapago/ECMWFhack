from readInAccidents import createDataFrameFromAccFile
from readInWeather import getMeteoValue
import numpy as np
import pickle

def combineSources():
    accidentsDF = createDataFrameFromAccFile()
    varList = ["tp","t2m","d2m","sf","fg10","u10","v10"]
    accidentsDF = accidentsDF.sort_values(by = "TimeStamp")
    #cols = accidentsDF[list("TimeStamp", "lat", "lon")]
    accidentsDF["tp"] = np.vectorize(getMeteoValue)("tp", accidentsDF["TimeStamp"], accidentsDF["lat"],accidentsDF["lon"])#precipitation
    accidentsDF["t2m"] = np.vectorize(getMeteoValue)("t2m", accidentsDF["TimeStamp"], accidentsDF["lat"],accidentsDF["lon"])#temperature
    accidentsDF["d2m"] = np.vectorize(getMeteoValue)("d2m", accidentsDF["TimeStamp"], accidentsDF["lat"],accidentsDF["lon"])#dewpoint
    accidentsDF["sf"] = np.vectorize(getMeteoValue)("sf", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                    accidentsDF["lon"])#snow
    accidentsDF["fg10"] = np.vectorize(getMeteoValue)("fg10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                    accidentsDF["lon"]) #gust
    accidentsDF["u10"] = np.vectorize(getMeteoValue)("u10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                      accidentsDF["lon"])#wind1
    accidentsDF["v10"] = np.vectorize(getMeteoValue)("v10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                      accidentsDF["lon"])#wind2
    return accidentsDF





sortedDF = combineSources()
sortedDF.to_pickle("wrangledData2006.p")

#with (open("wrangledData.p", "rb")) as openfile:
           # test22 = pickle.load(openfile)
           # print test22