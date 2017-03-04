from readInAccidents import createDataFrameFromAccFile
from readInWeather import getMeteoValue
import numpy as np

def combineSources():
    accidentsDF = createDataFrameFromAccFile()
    accidentsDF = accidentsDF.sort_values(by = "TimeStamp")
    #cols = accidentsDF[list("TimeStamp", "lat", "lon")]
    accidentsDF["tp"] = np.vectorize(getMeteoValue)("tp",accidentsDF["TimeStamp"],accidentsDF["lat"],accidentsDF["lon"])
    accidentsDF["t2m"] = np.vectorize(getMeteoValue)("t2m", accidentsDF["TimeStamp"], accidentsDF["lat"],accidentsDF["lon"])
    accidentsDF["d2m"] = np.vectorize(getMeteoValue)("d2m", accidentsDF["TimeStamp"], accidentsDF["lat"],accidentsDF["lon"])
    accidentsDF["sf"] = np.vectorize(getMeteoValue)("sf", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                    accidentsDF["lon"])
    accidentsDF["fg10"] = np.vectorize(getMeteoValue)("fg10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                    accidentsDF["lon"])
    accidentsDF["u10"] = np.vectorize(getMeteoValue)("u10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                      accidentsDF["lon"])
    accidentsDF["v10"] = np.vectorize(getMeteoValue)("v10", accidentsDF["TimeStamp"], accidentsDF["lat"],
                                                      accidentsDF["lon"])
    return accidentsDF





sortedDF = combineSources()
sortedDF.to_pickle("wrangledData.p")