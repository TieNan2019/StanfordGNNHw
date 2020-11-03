#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

import random


def _11_node_classification():
    loops = 2

    nodes = list(range(1, 11))
    edges = [
        (1, 2), (1, 3), (2, 3), (2, 4), (3, 6), (5, 6), (4, 7),
        (4, 8), (5, 8), (5, 9), (7, 8), (6, 9), (6, 10), (9, 10)
    ]

    # build the graph and initialize it with Pr = 0.5
    g = nx.Graph()
    g.add_nodes_from(nodes, Pr=0.5)
    g.add_edges_from(edges)

    # initialize postive nodes
    g.nodes[3]["Pr"] = 1
    g.nodes[5]["Pr"] = 1
    # initialize negative nodes
    g.nodes[8]["Pr"] = 0
    g.nodes[10]["Pr"] = 0

    nx.draw(g, with_labels=True)
    plt.savefig('_01_node_classification.png')

    # get the possibility of every node to be positive
    [nodes.remove(x) for x in [3, 5, 8, 10]]
    for i in range(loops):
        for node in nodes:
            g.nodes[node]["Pr"] = sum([g.nodes[node]["Pr"] for node in g[node]]) / len(g[node])

    # classification
    for node in g.nodes():
        g.nodes[node]["Class"] = "+" if g.nodes[node]["Pr"] > 0.5 else "-"

    return  g



if __name__ == "__main__":
    # 1.1. relational classification
    ans = _11_node_classification()
    print(ans.nodes.data())
