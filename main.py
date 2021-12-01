#Importing libraries
from igraph import *
from functions import *
from matplotlib import pyplot as plt
import numpy as np
#Defining parameters
n0 = 5 #Initial number ov vertices
m0 = 3 #Initial number of edges of a new vertex
times = [1,10,100,1000]
tmax = 10000


timeseries1,deg_seq1 = barabasi_growth_preferential(n0,m0,times,tmax)
#timeseries2,deg_seq2 = barabasi_growth_random(n0,m0,times,tmax)
#timeseries3,deg_seq3 = barabasi_no_growth(1000,2,times,tmax)

#write_file(timeseries1[0],"node1_growth_preferential.txt")
#write_file(timeseries1[1],"node2_growth_preferential.txt")
#write_file(timeseries1[2],"node3_growth_preferential.txt")
#write_file(timeseries1[3],"node4_growth_preferential.txt")
#write_file(timeseries2[0],"node1_growth_random.txt")
#write_file(timeseries2[1],"node2_growth_random.txt")
#write_file(timeseries2[2],"node3_growth_random.txt")
#write_file(timeseries2[3],"node4_growth_random.txt")
#write_file(timeseries3[0],"node1_no_growth.txt")
#write_file(timeseries3[1],"node2_no_growth.txt")
#write_file(timeseries3[2],"node3_no_growth.txt")
#write_file(timeseries3[3],"node4_no_growth.txt")
#write_file(deg_seq1,"deg_sequence_preferential.txt")
#write_file(deg_seq2,"deg_sequence_random.txt")
#write_file(deg_seq3,"deg_sequence_no_growth.txt")

#Visual comparison of Vertex Degree over Time and Ki'(t)

#Plot the K-ith for each vertex

scale2 = np.array(timeseries1[1])
scale3 = np.array(timeseries1[2])
scale4 = np.array(timeseries1[3])

plt.plot(timeseries1[0])
plt.title("1")
plt.show()

plt.plot(scale2*(10**0.5))
plt.title("2")
plt.show()

plt.plot(scale3*(100**0.5))
plt.title("3")
plt.show()

plt.plot(scale4*(1000**0.5))
plt.title("4")
plt.show()
