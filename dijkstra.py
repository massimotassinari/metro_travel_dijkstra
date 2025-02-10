def mas_corto(nodo, prev_cost, graph, t):
    """
    nodo ==> nodo a estudiar
    prev_cost ==> costo para llegar al nodo estudiado
    graph ==> lista de adyacencia
    t ==> tabla auxiliar

    return==> tabla auxiliar actualizada y el nodo siguiente

    Actualiza los pesos de los vecinos del nodo en
    el que te encuentras si es menor al previo"""
    sig = 0
    t[nodo][2] = True
    aux = ("AUX", 9999)
    for x in graph[nodo]:
        if t[x[0]][2] == False:
            if t[x[0]][0] > x[1] + prev_cost:
                t[x[0]][0] = x[1] + prev_cost
                t[x[0]][1] = nodo

            if x[1] + prev_cost < aux[1]:
                aux = (x[0], x[1] + prev_cost)

    return sig, t


def costo_minimo(graph, t, inicio, final):
    """
    inicio ==> aereopuerto inicio
    final ==> aereopuerto destino
    graph ==> lista de adyacencia
    t ==> tabla auxiliar

    return ==> lista de los aereopuertos a recorrer

    Actualiza los pesos de los vecinos del nodo en
    el que te encuentras si es menor al previo"""

    # inicializacion de la tabla auxiliar
    t = {x: [999, "", False] for x in graph.keys()}
    t[inicio[0]][0] = 0

    sig = inicio
    cont = True
    while cont:
        cont = False
        lista = []

        for key, nodo in t.items():
            if nodo[2] == False:
                lista.append((key, nodo[0]))
                cont = True
        lista.sort(key=lambda x: x[1])

        if len(lista) != 0:
            sig = lista[0]

            sig, t = mas_corto(sig[0], t[sig[0]][0], graph, t)

    return recorrido(final, t)


def recorrido(final, t):
    """
    final ==> aerepuerto destino
    t ==> tabla auxiliar final

    return ==> lista con la ruta de los aerepuertos

    A traves de la tabla auxiliar genera el recorrido de la misma en una lista"""
    cadena = [final]
    while final != "":
        cadena.append(t[final][1])

        final = t[final][1]

    return cadena[:-1][::-1]


"""
graph_min_escalas = {
    "AUA": [("CCS", 1), ("CUR", 1), ("BON", 1), ("SXM", 1)],
    "BGI": [("CCS", 1), ("POS", 1), ("SXM", 1)],
    "BON": [("CCS", 1), ("AUA", 1), ("CUR", 1)],
    "CCS": [("AUA", 1), ("CUR", 1), ("BON", 1), ("SDQ", 1), ("POS", 1), ("BGI", 1)],
    "CUR": [("CCS", 1), ("AUA", 1), ("BON", 1), ("SXM", 1)],
    "FDF": [("POS", 1)],
    "POS": [("CCS", 1), ("BGI", 1), ("SXM", 1), ("PTP", 1), ("FDF", 1)],
    "PTP": [("POS", 1), ("SXM", 1), ("SBH", 1)],
    "SBH": [("SXM", 1), ("PTP", 1)],
    "SDQ": [("CCS", 1), ("SXM", 1)],
    "SXM": [
        ("SDQ", 1),
        ("SBH", 1),
        ("POS", 1),
        ("BGI", 1),
        ("PTP", 1),
        ("CUR", 1),
        ("AUA", 1),
    ],
}
"""


def costo_recorrido(graph, recorrido):
    """
    graph ==> La lista de adyacencia correspondiente
    recorrido ==> la lista de aereopuertos del recorrido
    return ==> costo del recorido
    """
    costo = 0
    # la longitud del recorrido menos 1 para que no se pase del range
    for x in range(len(recorrido) - 1):
        # va agregando las rutas por pedazos para sacra el costo de cada tramo
        inicio = recorrido[x]
        fin = recorrido[x + 1]
        for y in graph[inicio]:
            # si y[0] que es el aereopuerto destino es igual a nuestro fin, agarramos el costo y lo sumamos al total
            if y[0] == fin:
                costo += y[1]

    return costo
