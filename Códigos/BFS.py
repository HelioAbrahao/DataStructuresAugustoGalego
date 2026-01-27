# DFS - Depth First Search - profundidade
# BFS - Breadth First Search - Amplitude
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
            
    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None: 
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
            
    def search(self, data): 
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def dfs(self, data):
        return self._dfs_recursive(self.root, data)
    
    def _dfs_recursive(self, node, data):
        if node:
            print(node.data)
        if node is None:
            return False
        if node.data == data:
            return True
        
        if self._dfs_recursive(node.left, data):
            return True
        
        if self._dfs_recursive(node.right, data):
            return True
    
    def bfs(self, data):
        if self.root is None: 
            return False
        
        queue = deque()
        queue.append(self.root)
        
        while queue: 
            node = queue.popleft()
            print(node.data)
            if node.data == data:
                return True
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
        return False
    
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)
tree.insert(20)

print("bfs:", tree.bfs(20))

