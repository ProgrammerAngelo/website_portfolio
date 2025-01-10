import networkx as nx
import tkinter as tk
from tkintermapview import TkinterMapView

# Define the stations with their coordinates (latitude, longitude) for LRT 1, LRT 2, and MRT 2
stations_coordinates = {
    # LRT 1
    "baclaran": (14.538825, 121.000683),
    "edsa": (14.538825, 121.000683),
    "libertad": (14.547783, 120.998631),
    "gil puyat": (14.554128, 120.997178),
    "vito cruz": (14.563475, 120.994681),
    "quirino": (14.570219, 120.991675),
    "pedro gil": (14.576631, 120.987992),
    "united nations": (14.582492, 120.984661),
    "central terminal": (14.592903, 120.981622),
    "carriedo": (14.599, 120.981358),
    "doroteo jose": (14.605475, 120.982069),
    "bambang": (14.611111, 120.9825),
    "tayuman": (14.616794, 120.982758),
    "blumentritt": (14.622728, 120.982889),
    "abad santos": (14.630617, 120.981414),
    "r. papa": (14.636086, 120.982308),
    "5th avenue": (14.644475, 120.983575),
    "monumento": (14.654094, 120.983906),
    "balintawak": (14.657344, 121.003961),
    "roosevelt": (14.657494, 121.021211),

    # LRT 2
    "recto": (14.6035, 120.9835),
    "legarda": (14.6009, 120.9926),
    "pureza": (14.6019, 121.0054),
    "v. mapa": (14.603889, 121.016944),
    "j. ruiz": (14.6106, 121.0262),
    "gilmore": (14.61333, 121.03389),
    "betty go-belmonte": (14.61833, 121.04250),
    "cubao-lrt2": (14.6228, 121.0530),  # Cubao for LRT 2
    "anonas": (14.6280, 121.0647),
    "katipunan": (14.6308, 121.0727),
    "santolan-lrt2": (14.622139, 121.085917),
    "marikina": (14.62028, 121.10028),
    "antipolo": (14.62472, 121.12111),

    # MRT 2
    "north avenue": (14.652444, 121.032167),
    "quezon avenue": (14.642444, 121.038674),
    "gma kamuning": (14.635144, 121.043361),
    "cubao-mrt2": (14.6195, 121.0511),  # Cubao for MRT 2
    "ortigas": (14.5876, 121.0566),
    "shaw boulevard": (14.581397, 121.053681),
    "boni": (14.573764, 121.048167),
    "guadalupe": (14.566861, 121.045467),
    "buendia": (14.554203, 121.034094),
    "ayala": (14.548942, 121.027672),
    "magallanes": (14.541786, 121.019233),
    "taft avenue": (14.537517, 121.001406),
    "santolan-mrt2": (14.607711, 121.056442)
}

# Create a graph
G = nx.Graph()

# Add stations to the graph
for station in stations_coordinates.keys():
    G.add_node(station, pos=stations_coordinates[station])

# Add edges between stations
connections = [
    # LRT 1 connections
    ("baclaran", "edsa"), ("edsa", "libertad"), ("libertad", "gil puyat"), ("gil puyat", "vito cruz"),
    ("vito cruz", "quirino"), ("quirino", "pedro gil"), ("pedro gil", "united nations"),
    ("united nations", "central terminal"), ("central terminal", "carriedo"), ("carriedo", "doroteo jose"),
    ("doroteo jose", "bambang"), ("bambang", "tayuman"), ("tayuman", "blumentritt"),
    ("blumentritt", "abad santos"), ("abad santos", "r. papa"), ("r. papa", "5th avenue"),
    ("5th avenue", "monumento"), ("monumento", "balintawak"), ("balintawak", "roosevelt"),

    # LRT 2 connections
    ("recto", "legarda"), ("legarda", "pureza"), ("pureza", "v. mapa"), ("v. mapa", "j. ruiz"),
    ("j. ruiz", "gilmore"), ("gilmore", "betty go-belmonte"), ("betty go-belmonte", "cubao-lrt2"),
    ("cubao-lrt2", "anonas"), ("anonas", "katipunan"), ("katipunan", "santolan-lrt2"),
    ("santolan-lrt2", "marikina"), ("marikina", "antipolo"),

    # MRT 2 connections
    ("north avenue", "quezon avenue"), ("quezon avenue", "gma kamuning"), ("gma kamuning", "cubao-mrt2"),
    ("cubao-mrt2", "santolan-mrt2"), ("santolan-mrt2", "ortigas"), ("ortigas", "shaw boulevard"), ("shaw boulevard", "boni"),
    ("boni", "guadalupe"), ("guadalupe", "buendia"), ("buendia", "ayala"), ("ayala", "magallanes"),
    ("magallanes", "taft avenue"),

    # Interchange connections
    ("doroteo jose", "recto"),  # LRT 1 to LRT 2
    ("cubao-lrt2", "cubao-mrt2")  # LRT 2 to MRT 2
]

for station1, station2 in connections:
    G.add_edge(station1, station2, weight=1)

# Function to plot the shortest path on a map using Tkinter
def plot_shortest_path_on_map(start, end):
    if start not in G or end not in G:
        print("Invalid stations. Please try again.")
        return

    # Find the shortest path
    shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')
    print(f"\nShortest path from {start.title()} to {end.title()}: {shortest_path}")

    # Create a Tkinter window
    root = tk.Tk()
    root.title("LRT/MRT Map")

    # Create a map widget
    map_widget = TkinterMapView(root, width=800, height=600, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    # Set the initial map position
    map_widget.set_position(14.5995, 120.9842)
    map_widget.set_zoom(13)

    # Plot all stations
    for station, coord in stations_coordinates.items():
        map_widget.set_marker(coord[0], coord[1], text=station.title())

    # Highlight the shortest path
    path_coords = [stations_coordinates[station] for station in shortest_path]
    for i in range(len(path_coords) - 1):
        map_widget.set_path([path_coords[i], path_coords[i + 1]])

    # Run the Tkinter event loop
    root.mainloop()

# Booking system function
def find_shortest_path():
    print("\nWelcome to the LRT/MRT Booking System")
    start = input("Enter your starting station: ").lower().strip()
    end = input("Enter your destination station: ").lower().strip()

    # Handle special cases for Cubao and Santolan
    if start in ["cubao", "santolan"] or end in ["cubao", "santolan"]:
        if start == "cubao" or end == "cubao":
            transport = input("Do you mean LRT (Cubao-LRT2) or MRT (Cubao-MRT2)? ").lower().strip()
            if transport == "lrt":
                start = "cubao-lrt2" if start == "cubao" else start
                end = "cubao-lrt2" if end == "cubao" else end
            elif transport == "mrt":
                start = "cubao-mrt2" if start == "cubao" else start
                end = "cubao-mrt2" if end == "cubao" else end
            else:
                print("Invalid choice. Please specify 'LRT' or 'MRT'.")
                return

        if start == "santolan" or end == "santolan":
            transport = input("Do you mean LRT (Santolan-LRT2) or MRT (Santolan-MRT2)? ").lower().strip()
            if transport == "lrt":
                start = "santolan-lrt2" if start == "santolan" else start
                end = "santolan-lrt2" if end == "santolan" else end
            elif transport == "mrt":
                start = "santolan-mrt2" if start == "santolan" else start
                end = "santolan-mrt2" if end == "santolan" else end
            else:
                print("Invalid choice. Please specify 'LRT' or 'MRT'.")
                return

    plot_shortest_path_on_map(start, end)

# Run the booking system
find_shortest_path()
