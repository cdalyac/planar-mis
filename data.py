import networkx as nx
import networkx.algorithms.approximation as apxa
import random
import matplotlib.pyplot as plt
import planarity
import os
from igraph import *

# global declarations
data = []

starting_vertices = 3
ending_vertices = 50
total_vertices = ending_vertices - starting_vertices
trials = 100

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

def sort_dict(d):
  'return a sorted list of tuples from the dictionary'
  return sorted(d.viewitems(), cmp=lambda x,y: cmp(x[1], y[1]))

def maximum_independent_set(graph):
	H = G.copy()
	n=H.__len__()
	e=H.edges()
	igraph = Graph(n=n,edges=e)
	alpha = igraph.alpha()
	#if n >= 5:
	#	plot(igraph,target=None,bbox=(0, 0, 600, 600))

	#independent_set_size = 0
	#while len(H.nodes()) > 0:
	#	sorted_degrees = sort_dict(H.degree(H.nodes()))
	#	lowest_degree_vertex = sorted_degrees[0][0]
	#	H.remove_nodes_from(H.neighbors(lowest_degree_vertex))
	#	H.remove_node(lowest_degree_vertex)
	#	independent_set_size += 1
	return alpha


for vertices in range(starting_vertices, ending_vertices + 1):
	print("Running test " + str(vertices - starting_vertices) + "/" + str(total_vertices))
	for i in range(trials):
		if i/float(trials) >= 0.65:
			edge_probability = random.uniform(0,0.5)
		else:
			edge_probability = random.uniform(0.5,1.0)

		G = make_planar_graph(vertices, edge_probability)

		max_indep_set = maximum_independent_set(G)
		#print max_indep_set
		#if vertices/float(ending_vertices) >=0.15:
			##planarity.planarity_networkx.draw(G, labels=True)
		#	nx.draw_networkx(G)
		#	plt.show()
		data.append((vertices, G.number_of_edges(), max_indep_set))

# sort the data by n(G), then by alpha(G), then by e(G)
data = sorted(data, key = lambda trial: (trial[0], trial[2], trial[1]))

# get rid of the old data before writing
# then open the file, and print add the header
os.remove(output_file) if os.path.exists(output_file) else None
output = open(output_file, 'w')
output.write("n(G)\te(G)\ta(G)\tmax(e)\tmin(a)\tmax(a)\n")

# add all data to the output file
for trial_num in range(len(data)):
	min_alpha = trial_num/100*100
	max_alpha = trial_num/100*100+99
	output.write(str(data[trial_num][0]) + "\t" + str(data[trial_num][1]) + "\t" + str(data[trial_num][2]) + "\t" + str(3*data[trial_num][0] - 6) + "\t" + str(data[min_alpha][2]) + "\t" + str(data[max_alpha][2]) + "\n")

# close the file and exit
output.close()