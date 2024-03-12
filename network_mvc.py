import networkx as nx
from networkx.algorithms.community import louvain_communities

"""
    A simple algorithm to select representative nodes in a correlation graph.
    Algorithm is customized and based on Page Rank, so running it each time may
        return different results (because of Page Rank implementation).
    Not sure if anyone else has similar ideas or procedures.
"""
def cleanGraph(currentGraph):
    from copy import deepcopy
    dG = deepcopy(currentGraph)
    poped = list(nx.isolates(dG))
    dG.remove_nodes_from(poped)
    if len(dG.nodes)==0:
        return None, poped
    else:
        return dG, poped

def simplePageRankMVC(currentGraph, mvc_list=[], random=True, bias=1e-5):
    """
        mvc_list: the final selected nodes, including the isolated nodes.

        Note: to use this recursive function, do use 'mvc_list=[]' every time when initiated.
        Note: this algorithm is similar but NOT minimum vertex cover (MVC). Real MVC covers all
            edges in the graph, while this algorithm only covers nodes. DO NOT confuse with MVC.
    """
    from copy import deepcopy
    from random import shuffle
    if currentGraph == None:
        return mvc_list
    # assuming that the input graph is a single graph without isolated nodes
    dG = deepcopy(currentGraph)
    # get the most influencial nodes
    ranks = nx.pagerank(dG, max_iter=1000)
    ranklist = [(n, m) for n, m in ranks.items()]
    maxvalue = max([n[1] for n in ranklist])
    toplist = [n[0] for n in ranklist if abs(n[1]-maxvalue)<bias]
    if random:
        shuffle(toplist)
    # get the associated nodes and remove all nodes
    pgrk_node = toplist[0]
    mvc_list.append(pgrk_node)
    removed_list = [pgrk_node]
    for neighbor in dG.adj[toplist[0]].keys():
        removed_list.append(neighbor)
    dG.remove_nodes_from(removed_list)
    # clean up the graph & remove isolated nodes
    dG, pop = cleanGraph(dG)
    for nd in pop:
        mvc_list.append(nd)
    # recursion
    if dG==None:
        return mvc_list
    else:
        return simplePageRankMVC(dG, mvc_list)