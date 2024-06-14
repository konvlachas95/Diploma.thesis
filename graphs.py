#!/usr/bin/env python3
import networkx as nx

############################
#Generate a 2D lattice graph with a von Neumann neighborhood structure
############################
def lattice_von_neumann(n):
    G = nx.grid_2d_graph(n, n)
    G = relabel(G)
    return G

############################
# Relabel the nodes of G with integer labels
############################
def relabel(G):
    labels = {}
    for k, x in enumerate(G):
        labels[x] = k
    G = nx.relabel_nodes(G, labels)
    return G
