# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def inorder(root): 
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
            
        return inorder(root.left)