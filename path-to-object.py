#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# Created By  : Alka Dash
# Email  : alka146@gmail.com
# Created Date: 25-04-2022
# version ='1.0'
# ---------------------------------------------------------------------------

# NetworkX is a Python library for studying graphs and networks.
# Pyplot is a collection of functions in the popular visualization package Matplotlib.
import networkx as nx
import matplotlib.pyplot as plt
import os

# Creating an empty graph
G = nx.Graph()
# Getting the current working directory
directory = os.fsencode(os.getcwd())


# Creating a graph from the config file
def create_graph():
    # Check if config file exists
    if os.path.exists('config.conf') or os.path.exists('config.cnf'):
        print('Config file found')
    else:
        print('Config file not found')
        os.abort()
    # If config file exists, draw graph from config file
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".conf") or filename.endswith(".cnf"):
            with open(filename) as conf_file:
                for line in conf_file:
                    all_nodes = line.replace(":", ", ").replace(" - ", ", ")
                    for node, next_node in zip(all_nodes.split(', '), all_nodes.split(', ')[1:]):
                        G.add_edge(node.replace("\n", ""), next_node.replace("\n", ""))
            continue
        else:
            continue


# Display the graph created from the config file
def display_graph():
    # The figure has 1 row, 2 columns, and this plot is the first plot.
    plt.subplot(1, 2, 1)
    # Draw graph
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.gcf().set_size_inches(18.5, 10.5)
    # Display graph
    plt.show()


# Display the shortest path to object from given location
def path_to_object():
    # User inputs for current location and object
    source = input("Please enter your Current location: ")
    target = input("Please enter the object you need to find: ")
    try:
        shortest_path = nx.shortest_path(G, source=source, target=target)
    except nx.exception.NodeNotFound as e:
        print(e)
        os.abort()
    print('The Shortest path is ', shortest_path)
    print('=================Follow the below Directions===============')
    for i, x in zip(shortest_path, shortest_path[1:]):
        if x == shortest_path[-1]:
            print('From', i, 'get the', x)
        else:
            print('From', i, 'lead your self to the', x)


if __name__ == "__main__":
    create_graph()
    path_to_object()
    display_graph()
