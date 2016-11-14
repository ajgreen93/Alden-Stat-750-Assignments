import numpy as np

class Node:
	def __init__(self,ID,properties = None,firstEdge = None):
		self.ID = ID
		self.firstEdge = firstEdge
		self.properties = properties
		
class Edge:
	def __init__(self,startNode, endNode,nextEdge = None,properties = None):
		self.startNode = startNode
		self.endNode = endNode
		self.properties = properties
		self.nextEdge = nextEdge
		
class Graph:
	def __init__(self,nodes = [],edges = []):
		self.nodes = {}
		for node in nodes:
			self.add_node(node)
		
		for edge in edges:
			self.add_edge(edge)
		
	def add_node(self,node):
		if not node in self.nodes:
			self.nodes[node.ID] = node
	def add_edge(self,edge):
		for chosenNode in [edge.startNode,edge.endNode]:
			copyEdge = Edge(edge.startNode,edge.endNode,edge.nextEdge,edge.properties)
			node = self.nodes[chosenNode]
			if not node.firstEdge:
				node.firstEdge = copyEdge
			else:
				copyEdge.nextEdge = node.firstEdge
				node.firstEdge = copyEdge
			
	
	def print_representation(self):
		for ID in self.nodes:
			node = self.nodes[ID]
			print node.ID, ":"
			edge = node.firstEdge
			while edge:
				print edge.startNode,edge.endNode, " ",
				edge = edge.nextEdge
			print '\n'

	def create_adj_matrix(self):
    ## this is the distinct exercise for my homework 10, 
    ## which I accidentally included on the same branch as for
    ## hwk9
		n = len(self.nodes)
		idx = dict((key,value) for (key,value) in zip(self.nodes.keys(),range(n)))
		
		adj_matrix = np.zeros(shape = (n,n), dtype = int)
		for ID in self.nodes:
			node = self.nodes[ID]
			edge = node.firstEdge
			while edge:
				adj_matrix[idx[edge.startNode],idx[edge.endNode]] = 1
				adj_matrix[idx[edge.endNode],idx[edge.startNode]] = 1
				edge = edge.nextEdge
		
		return adj_matrix


			
			
