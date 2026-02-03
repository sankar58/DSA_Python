class BSTree:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insert(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftNode is None:
            rootNode.leftNode = BSTree(value)
        else:
            insert(rootNode.leftNode, value)
    else:
        if rootNode.rightNode is None:
            rootNode.rightNode = BSTree(value)
        else:
            insert(rootNode.rightNode, value)
    return 'node successfully inserted'

BST = BSTree(None)
print(insert(BST, 70))
print(insert(BST, 60))
print(BST.data)           # 70
print(BST.leftNode.data)  # 60
