#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import random
import math


def _01_solve():
    n = 20
    m = 80

    g = nx.Graph()
    nodes = list(range(n))

    g.add_nodes_from(nodes)
    
    i = 0
    while i < m:
        picked = random.sample(nodes, 2)
        picked.sort()
        if picked not in g.edges():
            g.add_edge(*picked)
            i += 1
    
    nx.draw(g, with_labels=True)
    # plt.savefig('_01_Erd ̋os-R ́enyiRandomGraph.png')
    return g


def _02_solve():
    n = 20
    m = 35

    g = nx.Graph()

    nodes = list(range(n))
    nx.add_cycle(g, nodes)

    odds = []
    even = []
    for x in nodes:
        if x % 2 == 0:
            even += [x]
        else:
            odds += [x]
    
    nx.add_cycle(g, even)
    nx.add_cycle(g, odds)
    
    i = 0
    while i < m:
        picked = random.sample(nodes, 2)
        picked.sort()
        if picked not in g.edges():
            g.add_edge(*picked)
            i += 1
            

    nx.draw(g, with_labels=True)
    # plt.savefig('_02_SmallWorld.png')

    return g


def _03_solve():
    # 1. 从文件读取所有边
    g = nx.read_edgelist("ca-GrQc.txt",  create_using=nx.DiGraph())

    # 2. 采样
    g = nx.DiGraph(random.sample(g.edges(), 80))
    # print(g.edges())

    return g


def _11_solve():
    g1 = _01_solve()
    g2 = _02_solve()
    g3 = _03_solve()

    g = nx.Graph()
    g.add_edges_from(g1.edges())
    g.add_edges_from(g2.edges())

    # print(g.edges())


def _12_solve():
    g1 = _01_solve()
    g2 = _02_solve()

    g = nx.DiGraph()
    g.add_edges_from(g1.edges())
    g.add_edges_from(g2.edges())

    
    coe = dict()
    for node in g.nodes():
        k = 0
        neighbors = []
        for src, dst in g.edges():
            if src == node:
                k += 1
                neighbors += [dst]
        
        if k >= 2:
            c = 0
            for a in g.nodes():
                for b in g.nodes():
                    if (a, b) in g.edges() or (b, a) in g.edges():
                        c += 1
            coe[node] = 2 * c / (k * (k - 1))
        else:
            coe[node] = 0

    C = sum(coe.values()) / len(coe)
    return C, coe


if __name__ == "__main__":
    # 0.1. Erd ̋os-R ́enyi Random graph
    _01_solve()

    # 0.2. Small-World Random Network
    _02_solve()

    # 0.3. Real-World Collaboration Network
    _03_solve()

    # 1.1. Degree Distribution
    _11_solve()

    # 1.2. Clustering
    _12_solve()
