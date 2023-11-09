#!/usr/bin/env python3

from games import bargain
import graphs as gr
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


# variable parameters
beta = 3
alpha = 5
lamda = 0.2
J0 = [4, 1, 1]

# stable parameters initialization
n = 6
gamma = 0.1
N_tags = 1
N_epochs = 1000
num_runs = 1
lattice = "lattice_von_neumann"
node_size = 100
G = gr.lattice_von_neumann(n)


run_name = "_results_n={:}_beta={:}_gamma={:}_lamda={:}_alpha={:}_J0={:}_lattice={:}_tags={:}".format(n, beta, gamma, lamda, alpha, J0, lattice, N_tags)

game = bargain(G, beta=beta, gamma=gamma, lamda=lamda, alpha=alpha, J0=J0, folder=run_name, N_tags=N_tags)
for k in range(num_runs):
    game.play(N_epochs=N_epochs)
    # game.plot_graph(node_size=node_size)
    # game.plot_statistics()
    
game.plot_graph(node_size=node_size)
game.plot_statistics()
game.plot_simplex()
game.barplot_function()
