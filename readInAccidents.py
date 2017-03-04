import pandas as pandas
import pyproj
from datetime import date, timedelta, datetime, time



# Hours are read from the string format and if in the right format parsed.
## For non compliant format (i.e., "Onbekend" string situation) a 0 hour is set.
#   @param string representing the minute.
#   @return padded string
def convertHour(x):
    xx = ""
    try:
        xx = str(x).split("-")[1].split(".")[0]
    except IndexError:
        #print("error:" + x)
        xx = str(0)
    return(xx)


## Padding of the minute with a zero if represented by one digit.
## For non compliant format (i.e., "Onbekend" string situation) a 0 minute is set.
#   @param string representing the minute.
#   @return padded string
def padMinute(x):
    try:
        x =int(x)
        if (x <= 9):
            x = str.zfill(str(x), 2)
    except ValueError:
        #print("Error minute:"+x)
        x=0
    return str(x)



## Minute field (original from the dataset) is check for non compliant values.
#   @param string representing the minute.
#   @return string with TRUE if correct format, FALSE otherwise.
def isCorrect(x):
    if x=="Onbekend":
        x="FALSE"
    else:
        x="TRUE"
    return(x)






def createDataFrameFromAccFile():
    fileFirstAttemp = "data/testAccidents.csv"
    file = "data/accidentsFull.csv"
    dataFrame = pandas.read_csv(file)

    dataFrame["hour"] = dataFrame['Uur'].map(lambda x: convertHour(x))
    dataFrame["day"] = dataFrame["datum"].map(lambda x: str(x)[:2])
    dataFrame["month"] = dataFrame["datum"].map(lambda x: str(x)[2:5])
    dataFrame["year"] = dataFrame["datum"].map(lambda x: "20" + str(x)[5:])
    dataFrame["minute"] = dataFrame["minuut"].map(lambda x: padMinute(x))
    dataFrame["NoError"] = dataFrame["minuut"].map(lambda x: isCorrect(x))
    timeStampToConvert = dataFrame["year"] + dataFrame["month"] + dataFrame["day"] + dataFrame["hour"] + dataFrame["minute"]
    dataFrame["TimeStamp"] = pandas.to_datetime(timeStampToConvert, format='%Y%b%d%H%M', unit='s')
    ##definition of the projections
    wgs84 = pyproj.Proj("+init=EPSG:4326")
    epsg28992 = pyproj.Proj("+init=EPSG:28992")



    test = pyproj.transform(epsg28992,wgs84,dataFrame["X"].tolist(),dataFrame["Y"].tolist())
    dataFrame["lat"] = test[1]
    dataFrame["lon"] = test[0]

    #print(test)

    return(dataFrame)







#df=createDataFrameFromAccFile()
#print(df.year)
#print(len(df))













#print(dataFrame["Niveaukop"])

#print(test)
#print(pd.DataFrame.head(accidents,4))