import matplotlib.pyplot as plt

def display_graph(G, title="Graphe"):
    """Affiche un graphe simple."""
    G.plot()
    plt.title(title)
    plt.show()

def display_graph_with_signal(G, signal, title="Graphe avec signal"):
    """Affiche un graphe avec un signal coloré sur les nœuds."""
    G.plot_signal(signal, vertex_size=50)
    plt.title(title)
    plt.show()
