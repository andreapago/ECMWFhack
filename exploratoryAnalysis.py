import pickle
import ggplot
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

with (open("wrangledDataTest.p", "rb")) as openfile:
           df = pickle.load(openfile)

#print df[:100]


plt.figure()
plt.title("Dew point temperature")
df['d2m'].plot.hist()
plt.show()

plt.figure()
plt.title("Air temperature")
df['t2m'].plot.hist()
plt.show()


plt.figure()
plt.title("Time")

test = df['TimeStamp'].map(lambda x: x.hour)
test.plot.hist()
plt.show()


print df["TimeStamp"]


#df.iplot(kind='histogram', barmode='stack', bins=100, histnorm='probability')
# matplotlib.plot(pd.DataFrame.hist(df,column="tp"))
# matplotlib.pyplot.figure()
#hist.plot()           # print test22