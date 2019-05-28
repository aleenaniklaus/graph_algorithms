"""

Creator: Aleena Watson
Creation date: 4-21-19

Graph structure represented as an adjacency list
of arrays (array of arrays). Within the graph,
exists functions for manipulating graphs including:
- delete a vertex
- add an edge between two nodes
- delete an edge at a given vertex
- breadth first search on a node
- depth first search on a node (dfs(v))
- depth first search on the graph

This project is mainly for proof of concept work,
to aid in mathematical graph theory concepts and has
not been formulated with scalability at the forefront.
Eventually this code will be refactored and used with
SciPy for scalability and efficiency.

"""

# A class to represent the adjacency list of the node 
class AdjNode: 
	def __init__(self, data):
		self.vertex = data
		self.edge = 1
	# end
# end

# A class to represent a graph . A graph 
# is the list of the adjacency lists (also arrays).
# Size of the array will be the no. of the 
# vertices "V" 
class Graph:
	def __init__(self, size):
		self.size = size
		self.graph = [ [] for _ in range(self.size) ]
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
		for i in range(self.size):
			if i != vertex:
				while vertex in self.graph[i]:
					self.graph[i].remove(vertex)
				# end
			# end
		# end
		self.graph[vertex] = []

		for i in range(self.size):
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

	# Breadth First Search on a given node:
	# For each node in the subarray of v, visit
	# v[i]'s lists and store it in history[].
	# return true and the list created.
	def bfs(self, v):
		length = len(self.graph)
		visited = [False] * length
		todo_list = []
		history = []
		visited[v] = True
		todo_list.append(v)
		while len(todo_list) > 0:
			# get the next element of the subarray
			x = todo_list.pop(0)
			history.append(x)
			for j in self.graph[x]:
				if visited[j.vertex] == False:
					visited[j.vertex] = True
					todo_list.append(j.vertex)
				# end
			# end
		# end
		return True, history
	# end

	def dfs(self, v, end=None):
		length = len(self.graph)
		visited = [False] * length
		todo_list = []
		history = []
		todo_list.append(v)
		while len(todo_list) > 0:
			# get the next element of the subarray
			x = todo_list.pop(-1)
			# print(todo_list)
			if visited[x] == True:
				continue
			# end
			if end != None and x == end:
				return True, history
			# end
			visited[x] = True
			history.append(x)
			for j in reversed(self.graph[x]):
				todo_list.append(j.vertex)
			# end
		# end
		return True, history
	# end

	def find_cycle(self, v):
		for i in self.graph[v]:
			self.delete_edge(v, i.vertex)
			#TODO: rewrite dfs to return path taken
			result = self.dfs(i.vertex, v)[0]
			path = [v] + self.dfs(i.vertex, v)[1]
			if result == True:
				print("cycle")
				self.add_edge(v, i.vertex)
				return True, path
			# end
			self.add_edge(v, i.vertex)
		# end
		return False
	# end

	# dfs_helper() and dfs() adapted from
	# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
	def dfs_allHelper(self, v, visited):
		visited[v] = True
		print(v)

		for j in self.graph[v]:
			if visited[j.vertex] == False:
				self.dfs_allHelper(j.vertex, visited)
			# end
		# end
	# end

	def dfs_all(self):
		v = len(self.graph)
		visited = [False] * (v)
		for i in range(v):
			if visited[i] == False:
				# For debugging purposes, return false if dfs_helper()
				# fails to run, likewise, return true at the end of fn
				if self.dfs_helper(i, visited) == False:
					return False
				# end
			# end
		# end
		return True
	# end
  
	# Function to print the graph
	def print_list(self, v= None):
		for i in range(self.size):
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
size = 10
pg = Graph(size)
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
print(pg.find_cycle(0))

# size = 6
# house = Graph(size)
# house.add_edge(1,2)
# house.add_edge(1,5)
# house.add_edge(2,3)
# house.add_edge(2,5)
# house.add_edge(3,4)
# house.add_edge(5,4)

# print(house.find_cycle(1))

# pg.print_list()
# pg.delete_vertex(8)
# pg.delete_edge(0, 1)
# pg.cycle_finder()
# print(pg.dfs_all())
# print(pg.bfs(0))
# print(pg.dfs(1))
# pg.cycleFinder(1)
# print(pg.isCyclic())
# pg.print_list()
# pg.print_degreeSequence()