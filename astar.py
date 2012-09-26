

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
	visitedNodes = []
	toVisit = [[]]
	currentNode = startnode
	currentPath = [startnode]

	while True:
		visitedNodes.append(currentNode)
		for node in currentNode.neighbours:
			if node not in visitedNodes:
				newPath = copy.deepcopy(currentPath)
				newPath.append(node) 
				toVisit.append(newPath)
		sort(toVisit)			
		if len(currentPath) == 0:
			return []
		currentPath = toVisit.pop()
		currentNode = currentPath[len(currentPath)]
		if currentNode is endnode:
			return currentNode

		

