import networkx as nx
import random
import matplotlib.pyplot as plt
import planarity
import os

# global declarations
data = []

starting_vertices = 3
ending_vertices = 50
total_vertices = ending_vertices - starting_vertices
trials = 25

output_file = "data/output.txt"

def make_planar_graph(vertices, edge_probability):
	"""
	Returns a planar networkx graph with the specified 
	number of vertices and with edges chosen using
	the specified edge probability
	"""
	G = nx.fast_gnp_random_graph(vertices, edge_probability)
	G = planarity.planarity_networkx.pgraph_graph(G)
	G_nx = planarity.planarity_networkx.networkx_graph(G)

	while planarity.planarity_functions.is_planar(G) is not True:
		edge_removals = planarity.planarity_functions.kuratowski_edges(G)[:1]
		G_nx.remove_edges_from(edge_removals)
		G = planarity.planarity_networkx.pgraph_graph(G_nx)

	return G_nx

for vertices in range(starting_vertices, ending_vertices + 1):
	print("Running test " + str(vertices - starting_vertices) + "/" + str(total_vertices))
	for i in range(trials + 1):
		edge_probability = random.random()
		G = make_planar_graph(vertices, edge_probability)

		max_indep_set = len(nx.maximal_independent_set(G))
		data.append((vertices, G.number_of_edges(), max_indep_set))

# sort the data by n(G), then by e(G)
data = sorted(data, key = lambda trial: (trial[0], trial[1]))

# get rid of the old data before writing
# then open the file, and print add the header
os.remove(output_file) if os.path.exists(output_file) else None
output = open(output_file, 'w')
output.write("n(G)\te(G)\ta(G)\tmax(e)\n")

# add all data to the output file
for trial in data:
	output.write(str(trial[0]) + "\t" + str(trial[1]) + "\t" + str(trial[2]) + "\t" + str(3*trial[0] - 6) + "\n")

# close the file and exit
output.close()