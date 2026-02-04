from distutils.command.install import value

import myqueue

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
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=myqueue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftNode is not None:
                customQueue.enqueue(root.value.leftNode)
            if root.value.rightNode is not None:
                customQueue.enqueue(root.value.rightNode)

def searchNode(rootNode, nodevalue):
    if rootNode.data ==nodevalue:
        print("we have found the node value ")
    if rootNode.data <=nodevalue:
        if rootNode.leftNode.data ==value:
            print("we have found the node value ")
        else:
            searchNode(rootNode.leftNode)
    else:
        if rootNode.rightNode.data ==value:
            print("we have found the node value ")
        else:
            searchNode(rootNode.rightNode)
BST = BSTree(None)
insert(BST, 70)
insert(BST, 50)
insert(BST, 90)
insert(BST, 30)
insert(BST, 80)
insert(BST, 100)
insert(BST, 20)
insert(BST, 40)
levelorderTraversal(BST)