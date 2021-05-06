import networkx as nx 

f = open("amazon-meta.txt", "r")
Data=f.readline()
g=nx.Graph()
for ASIN in Data:
    while ASIN in similar:
        g.add_edge(ASIN, similar)
print(nx.info(g))
