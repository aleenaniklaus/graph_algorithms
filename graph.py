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

class Graph:
	def __init__(self, size):
		self.size = size
		self.graph = [ [] for _ in range(self.size) ]
	# end

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
				if j.vertex == vertex:
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
			top_todo = todo_list.pop(-1)
			if visited[top_todo] == True:
				continue
			# end

			# we will only enter this if statement if the optional
			# endpoint "end" has been passed in. This condition was
			# added in specifically for cycle_finder()
			if end != None and top_todo == end:
				return True, history
			# end
			visited[top_todo] = True
			history.append(top_todo)

			# taking the elements in reverse for the todo list is what
			# differentiates this dfs algo from bfs algo above
			for j in reversed(self.graph[top_todo]):
				todo_list.append(j.vertex)
			# end
		# end

		# solely for cycle finder
		if end != None:
			return False, history
		# end
		return True, history
	# end

	# returns the first cycle found at a given vertex. If the verticies
	# are added in ascending order, this function will return the cycle
	# correlated with its lowest number neighbor
	def cycle_finder(self, v):
		for i in [node for node in self.graph[v]]:
			self.delete_edge(v, i.vertex)
			result = self.dfs(i.vertex, v)[0]
			dfs_history = [v] + self.dfs(i.vertex, v)[1]
			if result == True:
				# print("Cycle Found!", dfs_history)
				self.add_edge(v, i.vertex)
				return True, dfs_history
			# end

			if result == False:
				# print("No cycle at ", dfs_history)
				self.add_edge(v, i.vertex)
			# end
		# end
		return False, []
	# end

	# given a cycle of verticies passed in,
	# deletes the cycle but leaves verticies
	def delete_cycle_edges(self, cycle):
		length = len(cycle)
		for i in range(length):
			self.delete_edge(cycle[i], cycle[(i+1) % length])
		# end
	# end

	# dfs_helper() and dfs() adapted from
	# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
	def dfs_geeks_helper(self, v, visited):
		visited[v] = True
		for j in self.graph[v]:
			if visited[j.vertex] == False:
				self.dfs_allHelper(j.vertex, visited)
			# end
		# end
	# end

	def dfs_geeks(self):
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

	def print_neighbors(self, v):
		print(v, "'s neighbors:")
		for i in self.graph[v]:
			print("{} ".format(i.vertex), end="")
		# end
		print('\n')
	# end

	# Function to print the graph
	def print_graph(self, v= None):
		for i in range(self.size):
			self.print_neighbors(i)
		# end
	# end

# end

# TODO: change graph so that the verticies are not also the
# INDICIES. For example, if you set size = 10 for the petersen
# graph and start your verticies at 1 you will have INDEX
# OUT OF RANGE when creating the graph! Gah!

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
list = pg.bfs(3)
print(list[1])

# size = 5
# house = Graph(size)
# house.add_edge(0,1)
# house.add_edge(0,4)
# house.add_edge(1,2)
# house.add_edge(1,4)
# house.add_edge(2,3)
# house.add_edge(4,3)

# size = 7
# balloon = Graph(size)
# balloon.add_edge(0,1)
# balloon.add_edge(0,3)
# balloon.add_edge(0,5)
# balloon.add_edge(1,2)
# balloon.add_edge(2,4)
# balloon.add_edge(3,4)
# balloon.add_edge(5,6)