''''''

# Pre-order traversal
def pre_order(node):
    ''''''
    if node is None:
        return []
    res = []

    def rec(node, path = None, res = None):
        print(node.data if node else '', [i.data for i in path])
        if res is None:
            res = []
        if path is None:
            path = []
        if node not in res:
            res.append(node)
        if node and node.left and node.left not in res:
            path.append(node)
            rec(node.left, path, res)
        elif node and node.right and node.right not in res:
            path.append(node)
            rec(node.right, path, res)
        if path:
            rec(path.pop(), path, res)

    rec(node, [], res)
    return [i.data for i in res]

# In-order traversal
def in_order(node):
    ''''''
    if node is None:
        return []
    res = []

    def rec(node, path = None, res = None):
        if res is None:
            res = []
        if path is None:
            path = []

        if node.left is None:
            res.append(node)

        if node and node.left and node.left not in res:
            path.append(node)
            rec(node.left, path, res)
            if node not in res:
                res.append(node)

        if node and node.right and node.right not in res:
            path.append(node)
            rec(node.right, path, res)
            if node not in res:
                res.append(node)

    rec(node, [], res)
    return [i.data for i in res]

# Post-order traversal
def post_order(node):
    ''''''
    return []
