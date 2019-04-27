

""" 
An initial file to represent the Graph as an adjacency list. 
An alternative to the adjacency list is a sparce matrix. While
using sparce matricies is common, syntax is overly complex as
you must use Numpy/SciPy. Since these graphs are for proof of
concept, there is no reason to use such powerful structures.
Additionally, the graphs will be small, thus the heavy-duty 
machinery behind Numpy is not necessary. 

Lastly, the main advantage of adjacency list over matrix is 
the running/space complexity is lower at O(n) (verses O(n^2)).

Creation date: 4-21-19
Reference:
https://www.geeksforgeeks.org/graph-and-its-representations/

"""

# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.edge = 1
    # end
# end

# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [ [] for _ in range(self.V) ]
    # end
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        self.graph[src].append(node)
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        self.graph[dest].append(node)

        # Optional: Print array adjacencies as they are added
        # print([len(self.graph[i]) for i in range(self.V)])
    # end
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
        	# Print length of array of graph[i]
            # print(len(self.graph[i]))
            print("Neighbors of {}".format(i), end="")
            for neighbor in self.graph[i]:
                print(" -> {}".format(neighbor.vertex), end="") 
            # end
            print(" \n")
        # end
    # end
# end
  
  
# Driver program to the above graph class 
# if __name__ == "__main__": 
#     V = 8
#     graph = Graph(V) 
#     graph.add_edge(1, 1) 
#     graph.add_edge(1, 2) 
#     graph.add_edge(1, 3) 
#     graph.add_edge(1, 4) 
#     graph.add_edge(1, 5) 
#     graph.add_edge(1, 6) 
#     graph.add_edge(1, 7) 
  
#     graph.print_graph() 
# # end

# Petersen Graph
V = 10
graph = Graph(V) 
graph.add_edge(0, 1) 
graph.add_edge(0, 4)
graph.add_edge(0, 5) 
graph.add_edge(1, 2) 
graph.add_edge(1, 6) 
graph.add_edge(2, 3) 
graph.add_edge(2, 7) 
graph.add_edge(3, 4) 
graph.add_edge(3, 8) 
graph.add_edge(4, 9)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(6, 8)
graph.add_edge(6, 9)
graph.add_edge(7, 9)

graph.print_graph()