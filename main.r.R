#Importing libraries
library(igraph)


#Barabasi Growth + Preferential Attachment

#Defining parameters
n0 <- 5 #Initial number ov vertices
m0 <- 2 #Initial number of edges of every new vertex

#Create an initial barabasi graph
g <- barabasi.game(50)
plot(g,vertex.label = NA)

#Simulation (We can use this section to simulate all the three different graphs)
t1 <- 1
t2 <- 10
t3 <- 100
t4 <- 1000
tmax <- 10^5

#Simulate from time=0 to time=tmax
for(time in 0:tmax){
  #At each time add a node using preferential attachment
  #For node attached at time t-i, monitor them
}



