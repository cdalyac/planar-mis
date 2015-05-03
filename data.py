import networkx as nx
import random
import matplotlib.pyplot as plt
import planarity

data = []

def make_graph(vertices, edge_probability):
	G = nx.fast_gnp_random_graph(vertices, edge_probability)
	G = planarity.planarity_networkx.pgraph_graph(G)

	return G

for vertices in range(3, 11):
	for i in range(5):
		edge_probability = random.uniform(0, 0.7)
		G = make_graph(vertices, edge_probability)
		while planarity.planarity_functions.is_planar(G) is not True:
			G = make_graph(vertices, edge_probability)

		G_nx = planarity.planarity_networkx.networkx_graph(G)
		max_indep_set = len(nx.maximal_independent_set(G_nx))
		data.append((vertices, G_nx.number_of_edges(), max_indep_set))

print data