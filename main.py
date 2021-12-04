# Importing libraries
import csv

import numpy
from igraph import *
from functions import *
from matplotlib import pyplot as plt
import numpy as np
#Defining parameters
n0 = 5 #Initial number ov vertices
m0 = 5 #Initial number of edges of a new vertex
times = [1,10,100,1000]
tmax = 1000
experiments = 5


#write_file(timeseries1[0],"node1_growth_preferential.txt")q
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
n1_res1 = []
n2_res1 = []
n3_res1 = []
n4_res1 = []
n1_res2 = []
n2_res2 = []
n3_res2 = []
n4_res2 = []



timeseries1,deg_seq1 = barabasi_growth_preferential(n0,m0,times,tmax)
timeseries2,deg_seq2 = barabasi_growth_random(n0,m0,times,tmax)
timeseries3,deg_seq3 = barabasi_no_growth(10000,2,times,tmax)
write_file(deg_seq1,"deg_sequence_preferential.txt")
write_file(deg_seq2,"deg_sequence_random.txt")
write_file(deg_seq3,"deg_sequence_no_growth.txt")

with open('timeseries_preferential.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(timeseries1)

#Visual comparison of Vertex Degree over Time and Ki'(t)

#Plot the K-ith for each vertex
n1_res1.append(timeseries1[0])
n2_res1.append(timeseries1[1])
n3_res1.append(timeseries1[2])
n4_res1.append(timeseries1[3])
n1_res2.append(timeseries2[0])
n2_res2.append(timeseries2[1])
n3_res2.append(timeseries2[2])
n4_res2.append(timeseries2[3])


res1=np.array([np.array(xi) for xi in n1_res1])
res2=np.array([np.array(xi) for xi in n2_res1])
res3=np.array([np.array(xi) for xi in n3_res1])
res4=np.array([np.array(xi) for xi in n4_res1])


#avg1 = np.average(res1, axis=0)
#avg2 = np.average(res2, axis=0)
#avg3 = np.average(res3, axis=0)
#avg4 = np.average(res4, axis=0)

#t = np.linspace(0,tmax,100)
#k = m0*(t**0.5)
# plot the function
#plt.plot(t,k, 'r')

#Comparing ki for Barabasi Preferential
# plt.plot(timeseries1[0],color="blue")
# plt.plot(np.array(timeseries1[1])*(10**0.5),color="red")
# plt.plot(np.array(timeseries1[2])*(100**0.5),color="green")
# plt.plot(np.array(timeseries1[2])*(1000**0.5),color="orange")
# plt.show()

#Comparing ki for Barabasi Random
# plt.plot(f(np.array(timeseries2[0]),n0,m0,1),color="blue")
# plt.plot(f(np.array(timeseries2[1]),n0,m0,10),color="red")
# plt.plot(f(np.array(timeseries2[2]),n0,m0,100),color="green")
# plt.plot(f(np.array(timeseries2[3]),n0,m0,100),color="orange")
# plt.show()

#Comparing ki for no Growth
plt.plot(np.array(timeseries3[0]),color="blue")
plt.plot(np.array(timeseries3[1]),color="red")
plt.plot(np.array(timeseries3[2]),color="green")
plt.plot(np.array(timeseries3[3]),color="orange")
plt.show()
