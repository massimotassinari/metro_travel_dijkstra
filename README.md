
# MetroTravel Route Optimization Project

## Overview
MetroTravel is a route optimization tool designed to help users find the best travel routes between airports. The app allows users to choose between minimizing cost or stopovers and considers travel restrictions like visa requirements. The interface is built with `tkinter`, and route calculations use Dijkstra's algorithm.

## Features
- **User Interface:** Developed with `tkinter`, offering user input options for origin, destination, visa requirements, and route type.
- **Route Options:** 
  - Lowest cost
  - Fewest stopovers
- **Travel Constraints:** Accounts for visa restrictions.
- **Graph Visualization:** Visualizes routes using `matplotlib` and `networkx`.

## Project Structure
- **Core Modules:**
  - UI and control logic in `main.py`
  - Graph algorithms in `dijkstra.py`
  - Graph visualization in `grafo.py`
  - Utility functions in `functions.py`
- **Data Files:**
  - `vuelos.csv`: Flight data (origin, destination, cost).
  - `visas.csv`: Visa requirement data.

## Requirements
- Python 3.x
- Libraries: `tkinter`, `matplotlib`, `networkx`, `csv`

## Usage
1. Run `main.py` to start the app.
2. Select airports, visa status, and route preference.
3. Click "Calcular Ruta" to get the route.
4. Click "Ver Ruta" to view the route graphically.

## Example
For a trip from Caracas (CCS) to Saint Martin (SXM) with visa restrictions, the app calculates and visualizes the optimal path.

## Future Improvements
- Dynamic data updates.
- Interactive map features.
- Additional constraints like layover times.

## License
This project is licensed under the MIT License.
