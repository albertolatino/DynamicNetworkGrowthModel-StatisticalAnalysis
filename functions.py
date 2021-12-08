from igraph import Graph
import numpy as np
from matplotlib import pyplot as plt
import random
import math


def nodes_probabilities(g: Graph):
    probabilities = []

    # For each node i compute the probability as: degree(i)/sum of all degrees.
    for node in g.vs:
        node_degree = node.degree()
        prob = node_degree / (2 * len(g.es))
        probabilities.append(prob)

    return probabilities


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def connect_node(g: Graph, m0: int):
    stubs = get_stubs(g)

    # The just added node is the (number_of_vertex-1)-th
    g.add_vertex(1)
    new_node = g.vs[g.vcount() - 1]

    # Pick m0 random nodes based on their occurences in the stubs (proportional to degree of nodes)
    for i in range(m0):
        # Select a target node
        target_id = random.choice(stubs)
        target_node = g.vs[target_id]

        # Connect the new node to target
        g.add_edge(new_node, target_node)
        # Remove all occurrences of the id of that node from stubs (no multiedges, cannot be chosen again)
        # stubs.remove(target_id)  # wrong implementation, only deletes first occurrence of target_id
        stubs = remove_values_from_list(stubs, target_id)  # correct implementation

    return new_node


def connect_node_random(g: Graph, m0: int):
    nodes = g.vs.indices

    g.add_vertex(1)
    new_node = g.vs[g.vcount() - 1]

    # Pick m0 random nodes based on their occurences in the stubs (proportional to degree of nodes)
    for i in range(m0):
        # Select a target node
        target_id = random.choice(nodes)
        target_node = g.vs[target_id]

        # Connect the new node to target
        g.add_edge(new_node, target_node)
        # Remove all occurrences of the id of that node from stubs (no multiedges, cannot be chosen again)
        # nodes.remove(target_id)  # wrong implementation, only deletes first occurrence of target_id
        nodes = remove_values_from_list(nodes, target_id)  # correct implementation

    return new_node


def connect_node_no_growth(g: Graph, m0: int):
    stubs = get_stubs(g)
    nodes = g.vs.indices

    source_id = random.choice(nodes)
    source_node = g.vs[source_id]
    # Remove source node from possible target nodes to avoid loops
    # stubs.remove(source_id)  # wrong implementation
    stubs = remove_values_from_list(stubs, source_id)

    # Pick m0 random nodes based on their occurences in the stubs (proportional to degree of nodes)
    for i in range(m0):
        # Select a target node
        # Remove first source_node so that LOOP TO BE REMOVED?
        target_id = random.choice(stubs)
        target_node = g.vs[target_id]

        # Connect the new node to target
        g.add_edge(source_node, target_node)
        # Remove the id of that node from stubs (no multiedges, cannot be chosen again)
        # stubs.remove(target_id)  # wrong implementation
        stubs = remove_values_from_list(stubs, target_id)

    return source_node


def get_stubs(g: Graph):
    stubs = []

    for edge in g.es:
        source_vertex_id = edge.source
        target_vertex_id = edge.target
        stubs.append(source_vertex_id)
        stubs.append(target_vertex_id)

    return stubs


def barabasi_growth_preferential(n0, m0, times, tmax):
    # Create an initial graph of n0 nodes
    #g = Graph.Barabasi(n=n0, m=m0, directed=False)
    g = Graph.Erdos_Renyi(n=n0, p=1)

    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    degree_sequence = []
    analyzed_nodes = []

    # Simulate from time=0 to time=tmax
    for time in range(1,tmax):

        # Add a new node, m0 must be <= n0
        new_node = connect_node(g, m0)

        # Start monitor the nodes
        if time in times:
            analyzed_nodes.append(new_node)

        # Update values
        for i in range(len(analyzed_nodes)):
            timeseries[i].append(analyzed_nodes[i].degree())

    # Get all the nodes after the simulation
    nodes = g.vs.indices
    for node in nodes:
        degree_sequence.append(g.vs[node].degree())

    return timeseries, degree_sequence


def barabasi_growth_random(n0, m0, times, tmax):
    # Create an initial graph of n0 nodes
    g = Graph.Barabasi(n=n0, m=m0, directed=False)
    #g = Graph.Erdos_Renyi(n=n0,p=1)
    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    degree_sequence = []
    analyzed_nodes = []
    #Select 4 random nodes ot be analyzed


    # Simulate from time=0 to time=tmax
    for time in range(tmax):

        # Add a new node, m0 must be <= n0
        new_node = connect_node_random(g, m0)

        # Start monitor the nodes
        if time in times:
            analyzed_nodes.append(new_node)

        # Update values
        for i in range(len(analyzed_nodes)):
            timeseries[i].append(analyzed_nodes[i].degree())

    # Get all the nodes after the simulation
    nodes = g.vs.indices
    for node in nodes:
        degree_sequence.append(g.vs[node].degree())

    return timeseries, degree_sequence


def barabasi_no_growth(n0, m0, times, tmax):
    # Create an initial graph of n0 nodes
    #g = Graph.Barabasi(n=n0, m=m0, directed=False)
    g = Graph.Erdos_Renyi(n=n0,m=m0)

    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    degree_sequence = []
    analyzed_nodes = [g.vs[0],g.vs[9],g.vs[49],g.vs[99]]


    # Simulate from time=0 to time=tmax
    for time in range(tmax):

        # Add a new node, m0 must be <= n0
        new_node = connect_node_no_growth(g, m0)

        # Update values
        for i in range(len(analyzed_nodes)):
            timeseries[i].append(analyzed_nodes[i].degree())

    # Get all the nodes after the simulation
    nodes = g.vs.indices
    for node in nodes:
        degree_sequence.append(g.vs[node].degree())

    return timeseries, degree_sequence


def write_file(data, filename: str):
    with open(filename, "w") as output:
        output.write(str(data).replace('[', '').replace(']', '').replace(', ', '\n'))


def f(timeseries,n0,m0,ti):
    f = lambda x : x + m0 * (math.log(n0 + ti - 1)) - m0
    vfunc = np.vectorize(f)
    return vfunc(timeseries)


def plot_growth_preferential(avg1,avg2,avg3,avg4,tmax,m0):
    #Comparing ki for Barabasi Preferential
    #plot the function
    t = np.linspace(1000,tmax,9001)
    k = m0*(t**0.5)
    plt.plot(t,k, 'black', label = "Function")
    plt.plot(t,avg1[999:],color="blue",label="Vertex t1")
    plt.plot(t,avg2[990:]*(10**0.5),color="red",label="Vertex t2")
    plt.plot(t,avg3[900:]*(100**0.5),color="green",label="Vertex t3")
    plt.plot(t,avg4*(1000**0.5),color="orange",label="Vertex t4")
    plt.xlim(1000, tmax)
    plt.xlabel('Time')
    plt.ylabel('Degree')
    plt.legend()
    plt.show()

def plot_growth_random(avg1,avg2,avg3,avg4,tmax,n0,m0):
    #Comparing ki for Barabasi Random
    t = np.linspace(1000,tmax,9001)
    k = m0*(np.log(m0+t-1))
    plt.plot(t,k, 'black', label = "Function")
    plt.plot(t,f(avg1[999:],n0,m0,1),color="blue",label="Vertex t1")
    plt.plot(t,f(avg2[990:],n0,m0,10),color="red",label="Vertex t2")
    plt.plot(t,f(avg3[900:],n0,m0,100),color="green",label="Vertex t3")
    plt.plot(t,f(avg4,n0,m0,1000),color="orange",label="Vertex t4")
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Degree')

    plt.show()

def plot_growth_random_full(avg1,avg2,avg3,avg4,tmax,n0,m0):
    #Comparing ki for Barabasi Random
    t = np.linspace(0,tmax,9001)
    k = m0*(np.log(m0+t-1))
    plt.plot(t,k, 'black', label = "Function")
    plt.plot(f(avg1,n0,m0,1),color="blue",label="Vertex t1")
    plt.plot(f(avg2,n0,m0,10),color="red",label="Vertex t2")
    plt.plot(f(avg3,n0,m0,100),color="green",label="Vertex t3")
    plt.plot(f(avg4,n0,m0,1000),color="orange",label="Vertex t4")
    plt.legend()
    #plt.xlim(1000, tmax)
    plt.xlabel('Time')
    plt.ylabel('Degree')

    plt.show()

def plot_no_growth(avg1,avg2,avg3,avg4,tmax,n0,m0):
    # #Comparing ki for no Growth
    t = np.linspace(0, tmax, 100)
    k = 2 * (m0 / 1000) * t
    plt.plot(t, k, 'black' , label = "Function")
    plt.plot(avg1, color="blue",label="Vertex 1")
    plt.plot(avg2, color="red",label="Vertex 2")
    plt.plot(avg3, color="green",label="Vertex 3")
    plt.plot(avg4, color="orange",label="Vertex 4")
    plt.xlabel('Time')
    plt.ylabel('Degree')
    plt.xlim(1000, tmax)
    plt.legend()
    plt.show()