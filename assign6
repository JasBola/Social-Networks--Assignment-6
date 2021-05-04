import networkx as nx 
import pandas as pd 




f = open("amazon-meta.txt", "r")
Data=f.readline()
g=nx.Graph()
for ASIN in Data:
    for similar in Data:
        g.add_edge(ASIN, similar)
    
print(nx.info(G))
