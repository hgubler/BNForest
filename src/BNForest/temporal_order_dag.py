import networkx as nx

def temporal_order_dag(ordering):
    """
    Function for specifying the causal DAG based on a temporal ordering.

    Parameters:
    ordering: list 
        list of lists containg the variable names in the order of the temporal ordering
    """
    dag = nx.DiGraph()
    for i in range(len(ordering)):
        for j in range(i+1, len(ordering)):
            for node1 in ordering[i]:
                for node2 in ordering[j]:
                    dag.add_edge(node1, node2)
    return dag