# Importing libraries
import csv

import numpy
from igraph import *
from functions import *
from matplotlib import pyplot as plt
import numpy as np
import math
#Defining parameters
n0 = 5 #Initial number ov vertices
m0 = 4 #Initial number of edges of a new vertex
times = [1,10,100,1000]
tmax = 10000
experiments = 15
#random.seed(42)

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
deg_res1 = []
n1_res2 = []
n2_res2 = []
n3_res2 = []
n4_res2 = []


for i in range(1,experiments):

    timeseries1,deg_seq1 = barabasi_growth_preferential(n0,m0,times,tmax)
    timeseries2,deg_seq2 = barabasi_growth_random(n0,m0,times,tmax)
    timeseries3,deg_seq3 = barabasi_no_growth(1000,5,times,tmax)


    #Save for each node the different timeseries obtained in each experiment
    n1_res1.append(timeseries3[0])
    n2_res1.append(timeseries3[1])
    n3_res1.append(timeseries3[2])
    n4_res1.append(timeseries3[3])
    deg_res1.append(deg_seq3)


#Convert to np array
res1=np.array([np.array(xi) for xi in n1_res1])
res2=np.array([np.array(xi) for xi in n2_res1])
res3=np.array([np.array(xi) for xi in n3_res1])
res4=np.array([np.array(xi) for xi in n4_res1])
deg=np.array([np.array(xi) for xi in deg_res1])

#Average time series
avg1 = np.average(res1, axis=0)
avg2 = np.average(res2, axis=0)
avg3 = np.average(res3, axis=0)
avg4 = np.average(res4, axis=0)
avg_deg = np.average(deg, axis=0)

plot_growth_preferential(avg1,avg2,avg3,avg4,tmax,m0)
plot_growth_random(avg1,avg2,avg3,avg4,tmax,n0,m0)
plot_growth_random_full(avg1,avg2,avg3,avg4,tmax,n0,m0)
plot_no_growth(avg1,avg2,avg3,avg4,tmax,n0,m0)

#WRITE FILES

# with open('timeseries_no_growth.txt', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows([avg1,avg2,avg3,avg4])


np.savetxt("node1_no_growth.txt",avg1,delimiter="\n",fmt='%f')
np.savetxt("node2_no_growth.txt",avg2,delimiter="\n",fmt='%f')
np.savetxt("node3_no_growth.txt",avg3,delimiter="\n",fmt='%f')
np.savetxt("node4_no_growth.txt",avg4,delimiter="\n",fmt='%f')
np.savetxt("deg_sequence_no_growth.txt",deg[0],delimiter="\n",fmt='%f')



