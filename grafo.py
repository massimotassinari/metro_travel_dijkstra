import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import functions as f
import random
import dijkstra as d


def obtain_edge_colors(resultado):
    edge_colors = {}
    for x in range(len(resultado) - 1):
        inicio = resultado[x]
        fin = resultado[x + 1]
        edge_colors[(inicio, fin)] = "r"
        edge_colors[(fin, inicio)] = "r"

    return edge_colors


def obtain_edges():
    rutas = f.read_csv("vuelos")
    edges = []
    for ruta in rutas:
        edges.append((ruta[0], ruta[1]))

    return edges


def obtain_airports():
    rutas = f.read_csv("vuelos")
    airports = f.get_airports(rutas)

    return airports


def plot_graph_with_edge_colors(edges, colors, node_positions):
    # Crea el grafo con las aristas y nodos
    image_file = "mapa.jpeg"
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(plt.imread(image_file), extent=[0, 15, 0, 10])
    G = nx.Graph()
    G.add_edges_from(edges)

    # crea una lista de colores por cada arista
    edge_colors = [colors.get(edge, "black") for edge in G.edges()]

    # Dibuja el grafo con los parametros dados
    nx.draw(
        G,
        node_positions,
        with_labels=True,
        edge_color=edge_colors,
        node_size=400,
        font_size=9,
        width=3,
        font_color="white",
    )

    # Lo muestra
    plt.show()
