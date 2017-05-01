from collections import defaultdict

class Graph:
    """
    A directed graph.

    Implement it as an adjacency list. A dictionary should map nodes
    to a set of nodes. An edge is a tuple: (from_node, to_node).
    """

    def __init__(self):
        """Initialize the graph data structure."""
        self.graph = defaultdict(list)

    def add_node(self, node):
        """Add a node to the graph, but there's no edges from it"""
        self.graph[node]
        
    def add_edge(self, edge):
        """An edge is a tuple of nodes. If the nodes don't exist, create
        them."""
        fr, to = edge
        self.add_node(fr)
        self.add_node(to)
        self.graph[fr].append(to)
        
    def remove_node(self, node):
        """Remove a node and all edges to and from it."""
        try:
            del self.graph[node]
        except KeyError:
            return False
            
        for e in filter(lambda edge: edge[1] == node, self.edges()):
            self.remove_edge(e)
        return True

    def remove_edge(self, edge):
        """Remove an edge."""
        fr, to = edge
        try:
            self.graph[fr].remove(to)
            return True
        except ValueError:
            return False

    def nodes(self):
        """Return a generator of all the nodes."""
        return (n for n in self.graph)

    def edges(self):
        """Return a generator of all edge tuples."""
        for node, edges in self.graph.items():
            for e in edges:
                yield node, e

    def __contains__(self, node):
        """Support the "in" operator. Return whether node is in the graph."""
        return node in self.graph

    def __getitem__(self, node):
        """Support graph[node] syntax. Return a list of edges."""
        return self.graph.get(node, False)
        