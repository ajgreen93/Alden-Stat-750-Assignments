import unittest
from graph_traversal import *

def test_node_entry():
	nodes  = [Node(i) for i in range(10)]
	edges = [Edge(i,i+1) for i in range(9)]
	graph = Graph(nodes,edges)
	nodeIds = [ID for ID in graph.nodes]
	return nodeIds
	
def test_edge_entry():
	nodes  = [Node(i) for i in range(2)]
	edges = [Edge(i,i+1) for i in range(1)]
	graph = Graph(nodes,edges)
	graphEdges = []
	for ID in graph.nodes:
		node = graph.nodes[ID]
		edge = node.firstEdge
		while edge:
			graphEdges.append([edge.startNode,edge.endNode])
			edge = edge.nextEdge
	
	return graphEdges
	
class tokenizeTests(unittest.TestCase):

	def test_nodes(self):
		self.assertEqual(test_node_entry(),range(10))
	
	def test_edges(self):
		self.assertEqual(test_edge_entry(),[[0,1],[0,1]])
		
if __name__ == '__main__':
	unittest.main()
