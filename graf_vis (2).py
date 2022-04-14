# Нужно сначала импортировать библиотеки 
#pip install networkx
#pip install pyvis

import networkx as nx
from pyvis.network import Network

graf1 = [(1,2,3), (1,3,5),(1,4,4),(2,3,3),(2,6,1),(3,4,1),(3,6,2),(4,5,7)]

G1= nx.DiGraph()
G1.add_weighted_edges_from(graf1)


net1 = Network()
net1.from_nx(G1)

for node in net1.nodes:
    node['shape'] = 'circle'
    print (node)
for ed in net1.edges:
    ed['label'] = ed['weight']
    print (ed)

net1.show_buttons()

net1.show("graf1_file.html")

