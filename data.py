import networkx as nx
import random
import matplotlib.pyplot as plt
import planarity
import os

# global declarations
data = []

starting_vertices = 3
ending_vertices = 10
trials = 5

output_file = "data/output.txt"

def make_graph(vertices, edge_probability):
	"""
	Returns a Planarity graph with the specified 
	number of vertices and with edges chosen with
	the specified edge edge probability
	"""
	G = nx.fast_gnp_random_graph(vertices, edge_probability)
	G = planarity.planarity_networkx.pgraph_graph(G)

	return G

for vertices in range(starting_vertices, ending_vertices + 1):
	for i in range(trials + 1):
		# try to make a planar graph
		# the edge probability's equation proceeds from trial-and-error
		edge_probability = random.uniform(0, 0.0091*(vertices**2) - 0.1488*vertices + 0.8092)
		G = make_graph(vertices, edge_probability)
		# continue to create graphs until we have one that is planar
		while planarity.planarity_functions.is_planar(G) is not True:
			G = make_graph(vertices, edge_probability)

		# convert the graph into a network_x graph, and find the independent set
		# append pertinent data to our dataset
		G_nx = planarity.planarity_networkx.networkx_graph(G)
		max_indep_set = len(nx.maximal_independent_set(G_nx))
		data.append((vertices, G_nx.number_of_edges(), max_indep_set))

# sort the data by n(G), then by e(G)
data = sorted(data, key = lambda trial: (trial[0], trial[1]))

# get rid of the old data before writing
# then open the file, and print add the header
os.remove(output_file) if os.path.exists(output_file) else None
output = open(output_file, 'w')
output.write("n(G)\te(G)\ta(G)\n")

# add all data
for trial in data:
	output.write(str(trial[0]) + "\t" + str(trial[1]) + "\t" + str(trial[2]) + "\n")

# close the file and exit
output.close()