#!/usr/bin/env python3

from games import bargain
import graphs as gr
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

########################
# Figure 4
########################

n = 6
beta = 2.0
gamma = 0.1
N_tags = 1
J0 = [ 1, 1, 4 ]
N_epochs = 2000
num_runs = 1
lattice = "lattice_von_neumann"
node_size = 100
G = gr.lattice_von_neumann(n)

run_name = "_results_n={:}_beta={:}_gamma={:}_J0={:}_lattice={:}_Ν={:}".format(n, beta, gamma, J0, lattice, N_tags)

game = bargain(G, beta=beta, gamma=gamma, J0=J0, folder=run_name, N_tags=N_tags)

for k in range(num_runs):
    game.play(N_epochs=N_epochs)
    # game.plot_graph(node_size=node_size)
    # game.plot_statistics()

game.plot_graph(node_size=node_size)
plt.pause(5)
game.plot_statistics()
plt.pause(5)
game.plot_simplex()
plt.pause(5)
