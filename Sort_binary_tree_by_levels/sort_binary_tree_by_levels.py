''''''
from collections import deque

def tree_by_levels(node):
    ''''''
    if node is None:
        return []
    res = [node.value]
    deq = deque()
    if node.left:
        deq.append(node.left)
    if node.right:
        deq.append(node.right)
    while deq:
        node = deq.popleft()
        res.append(node.value)
        if node.left:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)
    return res
