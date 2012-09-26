

class Node:

	neighbours = []

	distance = 0
	def __lt__(self, other): #Less than. 
		return self.distance < other.distance


class Path(list):
	nodes = []
	def __lt__ (self, other):
		return self.nodes[-1] < other.nodes[-1] #Compare two last nodes
	
	def __getslice__(self, i, j):
		return Path(nodes.__getslice__(i, j))

def findPath(startnode, endnode):
	visited_nodes = []
	to_visit = [[]]
	current_node = startnode
	current_path = [startnode]

	while True:
		visited_nodes.append(current_node)
		for node in current_node.neighbours:
			if node not in visited_nodes:
				new_path = copy.deepcopy(current_path)
				new_path.append(node) 
				to_visit.append(new_path)
		sort(to_visit)			
		if len(current_path) == 0:
			return []
		current_path = to_visit.pop()
		current_node = current_path[len(current_path)]
		if current_node is endnode:
			return current_node

		

