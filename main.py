import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Label
import grafo as g
import functions as f
import dijkstra as d

class Aplication(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("MetroTravel")
        main_window.geometry("700x420")
        self.imagen = PhotoImage(file = "metrotravel.png")
        main_window.background = Label(image = self.imagen, text = "fondo")
        main_window.background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        main_window.resizable(0,0)
        self.icono = tk.PhotoImage(file="MetroTravelicon.png")
        main_window.iconphoto(True, self.icono)

        
        self.origen = ttk.Combobox(
            state="readonly",
            values=["CCS","AUA","BON","CUR", "SXM", "SDQ","SBH","POS", "BGI", "FDF", "PTP"],
            )
    
        self.origen.place(
            x=117, y=159,
        )

        self.destino = ttk.Combobox(
            state="readonly",
            values=["CCS","AUA","BON","CUR", "SXM", "SDQ","SBH","POS", "BGI", "FDF", "PTP"]
        )
        self.destino.place(
            x=378, y=159,
        )

        self.visa = ttk.Combobox(
            state="readonly",
            values=["Si", "No"]
        )
        self.visa.place(
            x=117, y=272,
        )

        self.tipo_ruta = ttk.Combobox(
            state="readonly",
            values=["Ruta más barata", "Ruta con menos escalas"]
        )
        self.tipo_ruta.place(
            x=378, y=272
        )

        self.ruta = tk.Button(
            main_window,
            text = "Calcular Ruta",
            font = ("Inter", 14),
            bg = "#3c96c6",
            fg = "black",
            command= self.calcular,
            relief="flat",
        )

        self.ruta.place(
            x=311, y=358
        )

    def mostrar_grafo(self, resultado):
        # Define the edges and edge colors
        node_positions = {'AUA': (1.915, 2.9), 'BGI': (12.15, 3.71), 'BON': (3.618, 2.458), 'CCS': (4.724, 0.611), 'CUR': (2.81, 2.506), 'FDF': (10.958, 5.286), 'POS': (10.025,0.803), 'PTP': (10.574, 7.133), 'SBH': (9.785,8.769), 'SDQ': (6.331,8.971), 'SXM': (9.063, 9.250)}

        edges = g.obtain_edges()
        edge_colors = g.obtain_edge_colors(resultado)

        # Plot the graph with the edge colors

        g.plot_graph_with_edge_colors(edges, edge_colors,node_positions)
    
    def resultado_text(self,resultado):
        cadena = ""
        for x in range(len(resultado)):
            cadena+=resultado[x]
            cadena+= "-->"
        return cadena[:-3]
   
    def calcular(self):
        t = {}
        notes = f.read_csv("vuelos")
        airports = f.get_airports(notes)
        visas_list = f.read_csv("visas")

        seleccion_origen = self.origen.get()
        inicio = (seleccion_origen, 0)

        seleccion_final = self.destino.get()
        final = seleccion_final

        seleccion_visa = self.visa.get()
        visa = seleccion_visa

        seleccion_tipo = self.tipo_ruta.get()
        tipo_ruta = seleccion_tipo

        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.configure(background="#3893fd")
        ventana_secundaria.title("MetroTravel")
        ventana_secundaria.resizable(False,False)
        ventana_secundaria.config(width=700, height=220)
        
     
        if visa == None or tipo_ruta == None or inicio == None or final == None:
            resultado = "Error: verifique los datos"
            costo = "Error"
        
        elif visa == "Si" and tipo_ruta == "Ruta más barata":
            graph = f.create_adjacency_list(notes)
            print(graph)
                
            resultado = d.costo_minimo(graph, t, inicio, final)
            costo = d.costo_recorrido(graph, resultado)

        elif visa == "No" and tipo_ruta == "Ruta más barata":
            if f.inicio_visa(inicio[0], visas_list) or f.fin_visa(final, visas_list):
                resultado = "No puede iniciar/terminar el viaje"
                costo = "0"
            else:
                graph = f.create_adjacency_visas(visas_list, notes)
                print(graph)
                resultado = d.costo_minimo(graph, t, inicio, final)
                costo = d.costo_recorrido(graph, resultado)
        
        elif visa == "Si" and tipo_ruta == "Ruta con menos escalas":
            graph_min_escalas = f.create_adjacency_list_same_value_route(notes)
            print(graph_min_escalas)
            resultado = d.costo_minimo(graph_min_escalas, t, inicio, final)
            costo = d.costo_recorrido(graph_min_escalas, resultado)

        elif visa == "No" and tipo_ruta == "Ruta con menos escalas":
            if f.inicio_visa(inicio[0], visas_list) or f.fin_visa(final, visas_list):
                    resultado = "No puede iniciar/terminar el viaje"
                    costo = "0"
            else:
                graph_min_escalas = f.create_adjacency_visas_same_value_route(visas_list, notes)
                print(graph_min_escalas)
                resultado = d.costo_minimo(graph_min_escalas, t, inicio, final)
                costo = d.costo_recorrido(graph_min_escalas, resultado)

       
        self.recorrido = tk.Label(
            ventana_secundaria,
            text = "Recorrido: ",
            fg = "#17314e",
            bg="#3893fd",
            justify="center",
            font = ("Inter bold", 40),
            
            )
        self.recorrido.place(
            x=30, y=40,
        )
        if resultado == "No puede iniciar/terminar el viaje":
            self.resultados = tk.Label(
                ventana_secundaria,
                text = "No puede iniciar/terminar el viaje",
                fg = "white",
                bg="#3893fd",
                justify="center",
                font = ("Inter", 30),
                )
            self.resultados.place(
                x=220, y=50,
            )

        else:
            self.resultados = tk.Label(
                ventana_secundaria,
                text = self.resultado_text(resultado),
                
                fg = "white",
                bg="#3893fd",
                justify="center",
                font = ("Inter", 30),
                )
            self.resultados.place(
                x=220, y=50,
            )

        self.costo = tk.Label(
            ventana_secundaria,
            text = costo,
            fg = "white",
            bg="#3893fd",
            justify="center",
            font = ("Inter", 40),
            )
        self.costo.place(
            x=200, y=100,
        )
        self.costo2 = tk.Label(
            ventana_secundaria,
            text = 'Costo: ',
            fg = "#17314e",
            bg="#3893fd",
            justify="center",
            font = ("Inter bold", 40),
            
            )
        self.costo2.place(
            x=30, y=100,
        )
        self.vergrafo = tk.Button(
            ventana_secundaria,
            text="Ver Ruta",
            font = ("Inter", 24),
            
            bg = "white",
            fg = "#17314e",
            command= lambda: self.mostrar_grafo(resultado)
        )
        self.vergrafo.place(x=300, y=170)

main_window = tk.Tk()
app = Aplication(main_window)
app.mainloop()





