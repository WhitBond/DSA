from queue import Queue
from stack import Stack

class DSALinkedListNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.next = None

class DSALinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, label, value=None):
        new_node = DSALinkedListNode(label, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, label):
        current = self.head
        while current:
            if current.label == label:
                return current
            current = current.next
        return None

    def remove_first(self):
        if not self.head:
            raise ValueError("List is empty")
        else:
            label = self.head.label
            self.head = self.head.next
            return label

    def is_empty(self):
        return self.head is None

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class DSAGraphNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.adjacent = DSALinkedList()

class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()

    def add_vertex(self, label, value=None):
        if not self.has_vertex(label):
            new_vertex = DSAGraphNode(label, value)
            self.vertices.insert_last(label, new_vertex)
        else:
            raise ValueError(f"Vertex with label '{label}' already exists")

    def add_edge(self, label1, label2):
        vertex1 = self.vertices.find(label1)
        vertex2 = self.vertices.find(label2)
        if vertex1 and vertex2:
            if not self.is_adjacent(label1, label2):
                vertex1.adjacent.insert_last(label2)
                vertex2.adjacent.insert_last(label1)  # For undirected graph
            else:
                raise ValueError("Edge already exists")
        else:
            raise ValueError("One or both vertices not found")

    def has_vertex(self, label):
        return self.vertices.find(label) is not None

    def get_vertex_count(self):
        count = 0
        current = self.vertices.head
        while current:
            count += 1
            current = current.next
        return count

    def get_edge_count(self):
        count = 0
        current = self.vertices.head
        while current:
            count += current.value.adjacent.get_length()
            current = current.next
        return count // 2  # Divide by 2 for undirected graph

    def get_vertex(self, label):
        vertex_node = self.vertices.find(label)
        return vertex_node.value if vertex_node else None

    def get_adjacent(self, label):
        vertex_node = self.vertices.find(label)
        return vertex_node.value.adjacent if vertex_node else None
    def is_adjacent(self, label1, label2):
        vertex_node = self.vertices.find(label1)
        if vertex_node:
            adjacent_list = vertex_node.value.adjacent
            return label2 in [adjacent_node.label for adjacent_node in adjacent_list]
        else:
            return False

 

    def display_as_list(self):
        current = self.vertices.head
        while current:
            print(f"Vertex: {current.label}")
            adjacent_list = current.value.adjacent
            if adjacent_list.head:
                print("Adjacent Vertices:", end=" ")
                adj_node = adjacent_list.head
                while adj_node:
                    print(adj_node.label, end=" ")
                    adj_node = adj_node.next
                print()
            else:
                print("No adjacent vertices")
            print()
            current = current.next

    def display_as_matrix(self):
        vertex_count = self.get_vertex_count()
        matrix = [[0] * vertex_count for _ in range(vertex_count)]

        # Populate the matrix with edge information
        current_vertex = self.vertices.head
        index_map = {}
        index = 0
        while current_vertex:
            index_map[current_vertex.label] = index
            index += 1
            current_vertex = current_vertex.next

        current_vertex = self.vertices.head
        while current_vertex:
            current_adjacent = current_vertex.value.adjacent.head
            while current_adjacent:
                row = index_map[current_vertex.label]
                col = index_map[current_adjacent.label]
                matrix[row][col] = 1  # Assuming unweighted graph
                current_adjacent = current_adjacent.next
            current_vertex = current_vertex.next

        # Display the matrix
        print("Adjacency Matrix:")
        print(" ", end="")
        for label in index_map:
            print(label, end=" ")
        print()
        for i, row in enumerate(matrix):
            print(index_map[self.vertices.find(i).value.label], end=" ")
            for val in row:
                print(val, end=" ")
            print()

    def depthFirstSearch(self):
        T = DSALinkedList()
        S = Stack()
        self.clear_visited()

        current_vertex = self.vertices.head
        while current_vertex:
            if not current_vertex.value.visited:
                self.depthFirstSearch_recursive(current_vertex.value, T, S)
            current_vertex = current_vertex.next

        return T

    def depthFirstSearch_recursive(self, vertex, T, S):
        vertex.visited = True
        S.push(vertex)

        while not S.is_empty():
            current_vertex = S.peek()
            w = self.get_next_unvisited_adjacent(current_vertex)
            if w:
                T.insert_last(current_vertex.label, w.label)
                w.visited = True
                S.push(w)
            else:
                S.pop()

    def get_next_unvisited_adjacent(self, vertex):
        current = vertex.adjacent.head
        while current:
            if not self.vertices.find(current.label).visited:
                return self.vertices.find(current.label)
            current = current.next
        return None

    def breadthFirstSearch(self):
        T = DSALinkedList()
        Q = Queue()
        self.clear_visited()

        current_vertex = self.vertices.head
        while current_vertex:
            if not current_vertex.value.visited:
                self.breadthFirstSearch_recursive(current_vertex.value, T, Q)
            current_vertex = current_vertex.next

        return T

    def breadthFirstSearch_recursive(self, vertex, T, Q):
        vertex.visited = True
        Q.put(vertex)

        while not Q.empty():
            current_vertex = Q.get()
            while not current_vertex.adjacent.is_empty():
                w_label = current_vertex.adjacent.remove_first()
                w = self.vertices.find(w_label)
                if not w.visited:
                    T.insert_last(current_vertex.label, w_label)
                    w.visited = True
                    Q.put(w)

    def clear_visited(self):
        current_vertex = self.vertices.head
        while current_vertex:
            current_vertex.value.visited = False
            current_vertex = current_vertex.next

