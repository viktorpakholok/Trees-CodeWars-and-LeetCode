'''A solution of a problem "Delete Node in a BST"'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    '''Represents a node in a binary tree'''
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, \
right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''Provides solution to problem of deliting special node from binary search tree'''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ''' Delete the node with the given key from the binary search tree'''
        if root is None:
            return
        if root.val == key:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            cur_node = root.right
            while cur_node.left:
                cur_node = cur_node.left
            root.val = cur_node.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root
