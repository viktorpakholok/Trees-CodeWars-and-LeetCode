''''''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    ''''''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ''''''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ''''''
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
