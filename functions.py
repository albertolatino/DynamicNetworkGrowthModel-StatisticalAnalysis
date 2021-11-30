from igraph import Graph
import numpy as np
import random


def nodes_probabilities(g: Graph):
    probabilities = []

    # For each node i compute the probability as: degree(i)/sum of all degrees.
    for node in g.vs:
        node_degree = node.degree()
        prob = node_degree / (2 * len(g.es))
        probabilities.append(prob)

    return probabilities;


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

        #Connect the new node to target
        g.add_edge(new_node,target_node)
        #Remove the id of that node from stubs (no multiedges, cannot be chosen again)
        stubs.remove(target_id)

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
        # Remove the id of that node from stubs (no multiedges, cannot be chosen again)
        nodes.remove(target_id)

    return new_node


def connect_node_no_growth(g: Graph, m0: int):

    stubs = get_stubs(g)

    nodes = g.vs.indices

    source_id = random.choice(nodes)
    source_node = g.vs[source_id]
    #nodes.remove(target_id)

    # Pick m0 random nodes based on their occurences in the stubs (proportional to degree of nodes)
    for i in range(m0):
        # Select a target node
        # Remove first source_node so that LOOP TO BE REMOVED?
        target_id = random.choice(stubs)
        target_node = g.vs[target_id]

        # Connect the new node to target
        g.add_edge(source_node, target_node)
        # Remove the id of that node from stubs (no multiedges, cannot be chosen again)
        stubs.remove(target_id)

    return source_node

def get_stubs(g:Graph):

    stubs = []

    for edge in g.es:
        source_vertex_id = edge.source
        target_vertex_id = edge.target
        stubs.append(source_vertex_id)
        stubs.append(target_vertex_id)

    return stubs


def barabasi_growth_preferential(n0,m0,times,tmax):

    # Create an initial graph of n0 nodes
    g = Graph.Barabasi(n=n0, m=m0, directed=False)

    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    analyzed_nodes = []

    # Simulate from time=0 to time=tmax
    for time in range(tmax):

        # Add a new node, m0 must be <= n0
        new_node = connect_node(g, m0)

        # Start monitor the nodes
        if time in times:
            analyzed_nodes.append(new_node)

        # Update values
        for i in range(len(analyzed_nodes)):
            timeseries[i].append(analyzed_nodes[i].degree())

    return timeseries

def barabasi_growth_random(n0,m0,times,tmax):

    # Create an initial graph of n0 nodes
    g = Graph.Barabasi(n=n0, m=m0, directed=False)

    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    analyzed_nodes = []

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

    return timeseries

def barabasi_no_growth(n0,m0,times,tmax):

    # Create an initial graph of n0 nodes
    g = Graph.Barabasi(n=n0, m=m0, directed=False)

    # Lists that will contain the TimeSeries information for each one of the analyzed nodes
    # They are initialized with 0 since the degree as soon the node ia created is 0
    timeseries = [[0], [0], [0], [0]]
    analyzed_nodes = []

    # Simulate from time=0 to time=tmax
    for time in range(tmax):

        # Add a new node, m0 must be <= n0
        new_node = connect_node_no_growth(g, m0)

        # Start monitor the nodes
        if time in times:
            analyzed_nodes.append(new_node)

        # Update values
        for i in range(len(analyzed_nodes)):
            timeseries[i].append(analyzed_nodes[i].degree())

    return timeseries
