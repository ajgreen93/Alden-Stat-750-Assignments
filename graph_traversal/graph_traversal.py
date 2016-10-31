
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
			


			
			
