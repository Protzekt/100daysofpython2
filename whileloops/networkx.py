import networkx as nx

# Δημιουργία του γράφου
G = nx.DiGraph()

# Προσθήκη ακμών με βάρη
edges = [
    (1, 2, 4),
    (1, 4, 6),
    (1, 3, 3),
    (2, 5, 3),
    (3, 6, 6),
    (4, 2, 5),
    (4, 5, 2),
    (4, 7, 5),
    (5, 7, 2),
    (6, 7, 1),
    (6, 9, 5),
    (7, 8, 4),
    (7, 10, 2),
    (8, 11, 7),
    (9, 10, 2),
    (10, 11, 8),
    (7, 11, 7),
    (10, 8, 3)
]

for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Υπολογισμός της συντομότερης διαδρομής από τον κόμβο 1 στον κόμβο 11
source = 1
target = 11
shortest_path_length = nx.dijkstra_path_length(G, source, target)
shortest_path = nx.dijkstra_path(G, source, target)

# Εκτύπωση αποτελεσμάτων
print(f"Η συντομότερη διαδρομή από τον κόμβο {source} στον κόμβο {target} είναι: {shortest_path}")
print(f"Το μήκος της συντομότερης διαδρομής είναι: {shortest_path_length}")