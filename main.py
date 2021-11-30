#Importing libraries
from igraph import *
from functions import *
from matplotlib import pyplot as plt

#Defining parameters
n0 = 5 #Initial number ov vertices
m0 = 2 #Initial number of edges of a new vertex
times = [1,10,100,1000]
tmax = 10000


results = barabasi_growth_preferential(n0,m0,times,tmax)
#results_2 = barabasi_growth_random(n0,m0,times,tmax)
#results_3 = barabasi_no_growth(1000,2,times,tmax)



#CREATE 2 FILES: 1 degree sequence file, 2, four time series files

plt.plot(results[0])
plt.title("1")
plt.show()
plt.plot(results[1])
plt.title("2")
plt.show()
plt.plot(results[2])
plt.title("3")
plt.show()
plt.plot(results[3])
plt.title("4")
plt.show()
