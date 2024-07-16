import networkx as nx

def temporal_order_dag(ordering):
    dag = nx.DiGraph()
    for i in range(len(ordering)):
        for j in range(i+1, len(ordering)):
            for node1 in ordering[i]:
                for node2 in ordering[j]:
                    dag.add_edge(node1, node2)
    return dag