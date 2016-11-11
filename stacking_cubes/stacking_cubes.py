import pandas as pd

class Node:
	def __init__(self,ID):
		self.ID = ID
		self.sides = [0] * 6
		self.child = None

#stack is a list of two lists
#the first list gives all the ids of cubes in the stack
#the second list gives which side is facing up for each cubes
def find_max_stack(bottom_color = None,node = None,stack = [[],[]]):				
	matches = []
	matched_sides = []
	for i in range(6):
		if (i+1) % 2 == 1:
			if node.sides[i+1] == bottom_color:
				matches.append(node.sides[i])
				matched_sides.append(i+1)
                
		if (i+1) % 2 == 0:
			if node.sides[i-1] == bottom_color:
				matches.append(node.sides[i])
				matched_sides.append(i+1)
	
	if bottom_color is None:
		matches = node.sides
		matched_sides = range(1,7)
	
	max_stack = stack
	
	if matches: 
		for match,matched_side in zip(matches,matched_sides):
			test_stack = [[],[]]
			test_stack[0] = stack[0] + [node.ID]
			test_stack[1] = stack[1] + [matched_side]
			
			if node.child:
				test_stack = find_max_stack(bottom_color = match,node = node.child,stack = test_stack)
			
			if len(test_stack[0]) > len(max_stack[0]):
				max_stack = test_stack

	if node.child is not None:
		test_stack = find_max_stack(bottom_color,node.child,stack)
		if len(test_stack[0]) > len(max_stack[0]):
			max_stack = test_stack
	
	return max_stack
	
def output_max_stack(document):
	Head = Node(0)
	Parent = Head
	
	with open(document) as f:
		lines  = f.readlines()
		for i in range(0,len(lines)):
			node =  Node(i+1)
			node.sides  = map(int,lines[i].rstrip('\n').split(' '))
			Parent.child = node
			Parent = node
		
	max_stack = find_max_stack(node = Head.child)
	convert_to_letters = {1:'f',
						  2:'b',
						  3:'T',
						  4:'B',
						  5:'l',
						  6:'r'
						 }
	max_stack[1] = [convert_to_letters[index] for index in max_stack[1]]

	solution = str()
	for i in range(len(max_stack[1])):
		solution += str(max_stack[0][i]) + str(max_stack[1][i]) + ' '		

	return solution
