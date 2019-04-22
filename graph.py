

""" 
A Python program to demonstrate the adjacency 
list representation of the graph 

Creation date: 4-21-19
This code is contributed by Kanav Malhotra/GeeksForGeeks:
https://www.geeksforgeeks.org/graph-and-its-representations/

Advantage of adjacency list over matrix is the running/space
complexity is lower - O(n) (verses O(n^2))
"""

  

  
# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
    # end
# end
  
# Code from GeeksForGeeks start

# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V
    # end
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
    # end
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Neighbors of {}".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
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


# Code from GeeksForGeeks end
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