#!/usr/bin/env python3

from games import bargain
import graphs as gr
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


########################
# 1000 iterations per agent
########################


# Figure
# n = 11
# beta = 0.3
# gamma = 0.1
# lamda = 0.3
# N_tags = 1
# J0 = [ 4, 4, 4 ]
# N_epochs = 2000
# num_runs = 1
# lattice = "lattice_von_neumann"
# node_size = 100

# Figure b=1.0
n = 21
beta = 1.7
gamma = 0.1
lamda = 0.17
alpha = 1
N_tags = 1
J0 = [ 1, 1, 4 ]
N_epochs = 2000
num_runs = 1
lattice = "lattice_von_neumann"
node_size = 100

# Figure b=3.0
# n = 11
# beta = 3.0
# gamma = 0.1
# lamda = 0.3
# N_tags = 1
# J0 = [ 1, 1, 4 ]
# N_epochs = 2000
# num_runs = 1
# lattice = "lattice_von_neumann"
# node_size = 100

G = gr.lattice_von_neumann(n)

run_name = "_results_n={:}_beta={:}_gamma={:}_lamda={:}_alpha={:}_J0={:}_lattice={:}_Ν={:}".format(n, beta, gamma, lamda, alpha, J0, lattice, N_tags)

game = bargain(G, beta=beta, gamma=gamma, lamda=lamda, J0=J0, folder=run_name, N_tags=N_tags)

for k in range(num_runs):
    game.play(N_epochs=N_epochs)
    game.plot_graph(node_size=node_size)
    game.plot_statistics()
    

game.plot_graph(node_size=node_size)
plt.show()

game.plot_statistics()
plt.show()