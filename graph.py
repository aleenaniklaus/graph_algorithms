
"""

Creator: Aleena Watson
Creation date: 4-21-19

Graph structure represented as an adjacency list
of arrays. 

"""

# A class to represent the adjacency list of the node 
class AdjNode: 
	def __init__(self, data):
		self.vertex = data
		self.edge = 1
		self.degree = None
	# end
# end

# A class to represent a graph . A graph 
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
	# end

	def delete_vertex(self, vertex):
		for i in range(self.V):
			if i != vertex:
				while vertex in self.graph[i]:
					self.graph[i].remove(vertex)
				# end
			# end
		# end
		self.graph[vertex] = []

		for i in range(self.V):
			for j in self.graph[i]:
				# test: print vertices as you iterate
				# print("{} ".format(i), end="")
				# test: print neighbors as you iterate
				# print("{} ".format(j.vertex), end="")
				if j.vertex == vertex:
					# test: did you make it into endpoints of deleted vertex?
					# print("here")
					self.graph[i].remove(j)
				# end
			# end
		# end
	# end

	def delete_edge(self, u, v):
		for j in self.graph[u]:
			if j.vertex == v:
				self.graph[u].remove(j)
			# end
		# end
		for i in self.graph[v]:
			if i.vertex == u:
				self.graph[v].remove(i)
			# end
		# end
	# end

	# dfs_helper() and dfs() adapted from
	# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
	# uncomment print(v) to see traversal!

	def dfs_helper(self, v, visited):
		visited[v] = True
		print(v)

		for j in self.graph[v]:
			if visited[j.vertex] == False:
				self.dfs_helper(j.vertex, visited)
			# end
		# end
	# end

	def dfs(self):
		v = len(self.graph)
		visited = [False] * (v)
		for i in range(v):
			if visited[i] == False:
				self.dfs_helper(i, visited)
			# end
		# end
	# end


	# adapted from
	# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
	# 
	# TODO:
	# implement as a list of verticies (0...9) instead boolean values

	def isCyclic_helper(self, v, visited, parent):

		# TODO:
		# 1:
		# change function to not be recursive
		# store array of cyclic numbers and return it
		# to the calling function instead of returning
		# "True", if no cycle, return None
		#
		# 2:
		# add "degree" to AdjNode and avoid
		# cycling through graph if all degrees =1
		# except one node (ie: stars)
		
		visited[v] = True
		print(v)

		for i in self.graph[v]:
			if visited[i.vertex] == False:
				if self.isCyclic_helper(i.vertex, visited, v):
					return True
				# end
			elif parent != -1:
				return True
			# end
		# end
		del cycle
		return False
	#end

	def isCyclic(self):
		visited = [False] * self.V
		for i in range(self.V):
			if visited[i] == False:
				if self.isCyclic_helper(i, visited, -1) == True:
					return True
				# end
			# end
		# end
		return False
	# end

	def print_neighbors(self, vertex):
		print(vertex, ":")
		for neighbor in self.graph[vertex]:
			print("{}  ".format(neighbor.vertex), end="")
		# end
		print("\n")
	# end
  
	# Function to print the graph
	def print_adjacencyLists(self):
		for i in range(self.V):
			# Print length of array of graph[i]
			# print(len(self.graph[i]))
			self.print_neighbors(i)
		# end
	# end

	# TODO:
	# implement print degree sequence, but before this can be done
	# full implementation of degree counter must be completed

	# def print_degreeSequence(self):
	# 	for i in self.graph:
	# 		print("{} ".format(i.degree), end="")
	# 	# end
	# # end
# end

# Petersen Graph
V = 10
pg = Graph(V) 
pg.add_edge(0, 1)
pg.add_edge(0, 4)
pg.add_edge(0, 5)
pg.add_edge(1, 2)
pg.add_edge(1, 6)
pg.add_edge(2, 3)
pg.add_edge(2, 7)
pg.add_edge(3, 4)
pg.add_edge(3, 8)
pg.add_edge(4, 9)
pg.add_edge(5, 7)
pg.add_edge(5, 8)
pg.add_edge(6, 8)
pg.add_edge(6, 9)
pg.add_edge(7, 9)


# pg.print_adjacencyList()
# pg.delete_vertex(8)
# pg.delete_edge(0, 1)
# pg.cycle_finder()
pg.dfs()
pg.isCyclic()
# pg.print_adjacencyLists()
# pg.print_degreeSequence()
#comment