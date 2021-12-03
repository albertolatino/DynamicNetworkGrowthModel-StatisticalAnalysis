#Importing libraries
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
n1_res = []
n2_res = []
n3_res = []
n4_res = []


for i in range(1,experiments):

    timeseries1,deg_seq1 = barabasi_growth_preferential(n0,m0,times,tmax)
    timeseries2,deg_seq2 = barabasi_growth_random(n0,m0,times,tmax)
    timeseries3,deg_seq3 = barabasi_no_growth(1000,2,times,tmax)
    write_file(deg_seq1,"deg_sequence_preferential.txt")
    write_file(deg_seq2,"deg_sequence_random.txt")
    write_file(deg_seq3,"deg_sequence_no_growth.txt")

    #Visual comparison of Vertex Degree over Time and Ki'(t)

    #Plot the K-ith for each vertex
    n1_res.append(timeseries1[0])
    n2_res.append(timeseries1[1])
    n3_res.append(timeseries1[2])
    n4_res.append(timeseries1[3])


res1=np.array([np.array(xi) for xi in n1_res])
res2=np.array([np.array(xi) for xi in n2_res])
res3=np.array([np.array(xi) for xi in n3_res])
res4=np.array([np.array(xi) for xi in n4_res])


avg1 = np.average(res1, axis=0)
avg2 = np.average(res2, axis=0)
avg3 = np.average(res3, axis=0)
avg4 = np.average(res4, axis=0)

t = np.linspace(0,tmax,100)
k = m0*(t**0.5)
# plot the function
plt.plot(t,k, 'r')
plt.plot(avg1,color="blue")
plt.plot(avg2*(10**0.5),color="red")
plt.plot(avg3*(100**0.5),color="orange")
plt.plot(avg4*(1000**0.5),color="black")
plt.show()
