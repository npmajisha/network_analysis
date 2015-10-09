__author__ = 'Majisha'
import sys
from scipy import stats
import networkx as nx

def compare_spearmanr(centrality1, centrality2):
    sorted_centrality1 = [x[0] for x in sorted(centrality1.items(),key = lambda x:(-x[1],x[0]))]
    sorted_centrality2 = [x[0] for x in sorted(centrality2.items(),key = lambda x:(-x[1],x[0]))]
    spearman_values = stats.spearmanr(sorted_centrality1,sorted_centrality2)
    rho = spearman_values[0]
    pval = spearman_values[1]
    print("rho value:"+str(rho)+ " "+"pval:"+str(pval))
    return


def write_to_file(filename, centrality):
    output_file = open(filename,"a")
    sorted_centrality = sorted(centrality.items(),key = lambda x:(-x[1],x[0]))
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
        Graph = nx.read_gml(input_file,relabel=False)

    input_file.close()

    #calculate network centrality for this graph
    print("Computing betweenness centrality")
    betweenCentrality = nx.betweenness_centrality(Graph)
    write_to_file("betweenness_"+str(type), betweenCentrality)

    print("Computing eigen vector centrality")
    eigenVectorCentrality = nx.eigenvector_centrality(Graph,max_iter=100)
    write_to_file("eigenvector_"+str(type), eigenVectorCentrality)

    print("Computing page rank centrality")
    pageRankCentrality = nx.pagerank(Graph,alpha=0.85,max_iter=100)
    write_to_file("pagerank_"+str(type), pageRankCentrality)

    print("Computing degree centrality")
    degreeCentrality = nx.degree_centrality(Graph)
    write_to_file("degree_"+str(type), degreeCentrality)

    print("Computing clustering coefficient")
    clusteringCoefficient = nx.clustering(Graph)
    write_to_file("clustering_"+str(type), clusteringCoefficient);

    #calculating dispersion scores
    if type == 2:
        print("Computing dispersion scores for Kringel")
        dispersionScore = nx.dispersion(Graph,20)
        write_to_file("dispersion_Kringel", dispersionScore)

        print("Computing dispersion scores for Trigger")
        dispersionScore = nx.dispersion(Graph,51)
        write_to_file("dispersion_Trigger", dispersionScore)

        print("Computing dispersion scores for SN4")
        dispersionScore = nx.dispersion(Graph,37)
        write_to_file("dispersion_SN4", dispersionScore)
    else:
        print("Computing dispersion scores for 107")
        dispersionScore = nx.dispersion(Graph,"107")
        write_to_file("dispersion_107", dispersionScore)

        print("Computing dispersion scores for 414")
        dispersionScore = nx.dispersion(Graph,"414")
        write_to_file("dispersion_414", dispersionScore)

        print("Computing dispersion scores for 698")
        dispersionScore = nx.dispersion(Graph,"698")
        write_to_file("dispersion_698", dispersionScore)

    #comparison
    print("Comparing Degree Centrality and Page Rank Centrality")
    compare_spearmanr(degreeCentrality, pageRankCentrality)
    print("Comparing Degree Centrality and Betweenness Centrality")
    compare_spearmanr(degreeCentrality, betweenCentrality)
    print("Comparing Degree Centrality and Eigen vector Centrality")
    compare_spearmanr(degreeCentrality, eigenVectorCentrality)
    print("Comparing clustering Centrality and Page Rank Centrality")
    compare_spearmanr(clusteringCoefficient, pageRankCentrality)
    print("Comparing clustering Centrality and Betweenness Centrality")
    compare_spearmanr(clusteringCoefficient, betweenCentrality)
    print("Comparing clustering Centrality and Eigen vector Centrality")
    compare_spearmanr(clusteringCoefficient, eigenVectorCentrality)


    return

#boilerplate for main
if __name__ == '__main__':
    main()