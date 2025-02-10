import csv


def read_csv(file_name):
    notes = ""
    # with open("metrotravel/" + file_name + ".csv", newline="") as f:
    with open(file_name + ".csv", newline="") as f:
        data = csv.reader(f, delimiter=",")
        notes = list(data)
    return notes


def fin_visa(final, visas_list):
    req_visa = [x[0] for x in visas_list if x[2] == "Requiere Visa"]

    if final in req_visa:
        return True
    else:
        return False


def inicio_visa(inicio, visas_list):
    req_visa = [x[0] for x in visas_list if x[2] == "Requiere Visa"]

    if inicio in req_visa:
        return True
    else:
        return False


def get_airports(lista):
    """
    lista ==> lista obtenida del csv de vuelos

    Retorna una lista de los aerepuertos a traves de la lista
    obtenida de la lectura del cvs de vuelos origen-destino-costo"""
    airports = set()
    for x in lista:
        airports.add(x[0])
        airports.add(x[1])

    airports = list(airports)
    airports = sorted(airports)
    return airports


# Si visa / min costo
def create_adjacency_list(lista):
    airports = get_airports(lista)

    dict_graph = {key: [] for key in airports}

    for vuelo in lista:
        dict_graph[vuelo[0]].append((vuelo[1], float(vuelo[2])))
        dict_graph[vuelo[1]].append((vuelo[0], float(vuelo[2])))

    return dict_graph


# Si visa / min escalas
def create_adjacency_list_same_value_route(lista):
    airports = get_airports(lista)

    dict_graph = {key: [] for key in airports}

    for vuelo in lista:
        dict_graph[vuelo[0]].append((vuelo[1], 1))
        dict_graph[vuelo[1]].append((vuelo[0], 1))

    return dict_graph


# No visa /costo minimo
def create_adjacency_visas(visas_list, lista):
    req_visa = [x[0] for x in visas_list if x[2] == "Requiere Visa"]

    airports = get_airports(lista)

    dict_graph = {key: [] for key in airports}

    for vuelo in lista:
        if vuelo[1] in req_visa:
            dict_graph[vuelo[0]].append((vuelo[1], 9999))

        if vuelo[0] in req_visa:
            dict_graph[vuelo[1]].append((vuelo[0], 9999))

        if vuelo[1] not in req_visa:
            dict_graph[vuelo[0]].append((vuelo[1], float(vuelo[2])))

        if vuelo[0] not in req_visa:
            dict_graph[vuelo[1]].append((vuelo[0], float(vuelo[2])))

    return dict_graph


# No visa /min escalas
def create_adjacency_visas_same_value_route(visas_list, lista):
    req_visa = [x[0] for x in visas_list if x[2] == "Requiere Visa"]

    airports = get_airports(lista)

    dict_graph = {key: [] for key in airports}

    for vuelo in lista:
        if vuelo[1] in req_visa:
            dict_graph[vuelo[0]].append((vuelo[1], 9999))

        if vuelo[0] in req_visa:
            dict_graph[vuelo[1]].append((vuelo[0], 9999))

        if vuelo[1] not in req_visa:
            dict_graph[vuelo[0]].append((vuelo[1], 1))

        if vuelo[0] not in req_visa:
            dict_graph[vuelo[1]].append((vuelo[0], 1))

    return dict_graph
