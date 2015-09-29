__author__ = 'Majisha'
import sys
import networkx as nx
import pickle

def write_to_file(filename, centrality):
    output_file = open(filename,"a")
    sorted_centrality = sorted(centrality.items(),key = lambda x:(x[1],x[0]), reverse=True)
    for key, value in sorted_centrality:
        output_file.write(str(key)+" "+str(value)+"\n")
    output_file.close()
    return

def main():
    #inputFile - network input
    file_path = sys.argv[1]
    input_file = open(file_path,"rb")

    type = 0
    if file_path.endswith('.txt'):
        type = 1
        #read as edge list
        Graph = nx.read_edgelist(input_file)
    elif file_path.endswith('.gml'):
        type = 2
        #read as gml
        Graph = nx.read_gml(input_file)

    input_file.close()


    #calculate network centrality for this graph
    print("Computing betweenness centrality")
    betweenCentrality = nx.betweenness_centrality(Graph)
    print(betweenCentrality)
    write_to_file("betweenness_"+str(type), betweenCentrality)

    print("Computing eigen vector centrality")
    eigenVectorCentrality = nx.eigenvector_centrality(Graph)
    print(eigenVectorCentrality)
    write_to_file("eigenvector_"+str(type), eigenVectorCentrality)

    print("Computing page rank centrality")
    pageRankCentrality = nx.pagerank(Graph)
    print(pageRankCentrality)
    write_to_file("pagerank_"+str(type), pageRankCentrality)

    print("Computing degree centrality")
    degreeCentrality = nx.degree_centrality(Graph)
    print(degreeCentrality)
    write_to_file("degree_"+str(type), degreeCentrality)


    return

#boilerplate for main
if __name__ == '__main__':
    main()