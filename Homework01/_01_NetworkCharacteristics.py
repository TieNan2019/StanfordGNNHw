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
    plt.savefig('_01_Erd ̋os-R ́enyiRandomGraph.png')


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
    plt.savefig('_02_SmallWorld.png')


def _03_solve():
    # 1. 从文件读取所有边
    g = nx.read_edgelist("ca-GrQc.txt",  create_using=nx.DiGraph())

    # 2. 采样
    g = nx.DiGraph(random.sample(g.edges(), 80))
    print(g.edges())


if __name__ == "__main__":
    # 1. Erd ̋os-R ́enyi Random graph
    # _01_solve()

    # 2. Small-World Random Network
    # _02_solve()

    # 3. Real-World Collaboration Network
    _03_solve()
