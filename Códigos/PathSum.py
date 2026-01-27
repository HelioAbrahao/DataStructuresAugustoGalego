# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if root.left is None and root.right is None: 
            if root.val == targetSum:
                return True
            else:
                return False
            
        restante = targetSum - root.val
        
        esquerda_tem = self.hasPathSum(root.left, restante)
        direita_tem = self.hasPathSum(root.right, restante)
        
        if esquerda_tem or direita_tem:
            return True
        else:
            return False
            
        
        
        