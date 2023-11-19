import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()

#количество вершин случайным образом
num_nodes = random.randint(3, 10)
for i in range(num_nodes):
    G.add_node(i)

#ребра между вершинами случайным образом
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        if random.random() < 0.5:  #вероятность наличия ребра - 1/2
            G.add_edge(i, j, weight=random.randint(1, 15)) #случайная длинна ребра

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
plt.show()