from generate_graph import generate_random_graph, generate_ring_graph
from display_graph import display_graph, display_graph_with_signal
from process_graph import add_signal_with_noise, apply_low_pass_filter, smoothness_calcul

def main():
    # Générer un graphe aléatoire
    G = generate_random_graph(n_nodes=15)

    # Afficher le graphe
    display_graph(G, title="Graphe aléatoire")

    # Ajouter un signal avec du bruit
    signal = add_signal_with_noise(G, signal_strength=1, noise_level=0.5)
    display_graph_with_signal(G, signal, title="Signal bruité")

    # Appliquer un filtre passe-bas
    filtered_signal = apply_low_pass_filter(G, signal)
    display_graph_with_signal(G, filtered_signal, title="Signal filtré")
    
    # Calcul de la smoothness
    smoothness_signal = smoothness_calcul(G, signal)
    smoothness_filtered_signal = smoothness_calcul(G, filtered_signal)
    print(f"Smoothness du signal bruité : {smoothness_signal}")
    print(f"Smoothness du signal filtré : {smoothness_filtered_signal}")

if __name__ == "__main__":
    main()
