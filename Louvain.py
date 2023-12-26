import networkx as nx
import community  # This is the python-louvain library
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import time

start_time = time.time()

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6),(6, 7), (7, 8), (2, 9), (5, 10), (9, 11), (3, 8), (11,12 )])

# Apply Louvain algorithm for graph partitioning
partition = community.best_partition(G)

# Visualize the partitioned graph
partitioned_graph = nx.Graph()
partitioned_graph.add_nodes_from(G.nodes, partition=list(partition.values()))
partitioned_graph.add_edges_from(G.edges)

# Create an interactive plot using matplotlib.pyplot
pos = nx.spring_layout(partitioned_graph)

fig, ax = plt.subplots()
nx.draw(partitioned_graph, pos, with_labels=True, font_weight='bold', node_color=list(partition.values()), cmap=plt.cm.get_cmap("viridis"), node_size=800, ax=ax)

graph_title = "Partitioned Graph (Louvain Algorithm)"
plt.title(graph_title, fontsize = 14, y = 1.05)


button_text = 'Efficiency'
button_ax = plt.axes([0.7, 0.01, 0.2, 0.05])  # [left, bottom, width, height]
button = Button(button_ax, button_text, color='#D8D252', hovercolor='#D86A52')

# Function to be called when the button is clicked
def on_button_click(event):
    button.label.set_text('O(m log n)')


# Connect the button click event to the function
button.on_clicked(on_button_click)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

plt.tight_layout()  # Ensure tight layout to prevent overlapping



plt.show()

