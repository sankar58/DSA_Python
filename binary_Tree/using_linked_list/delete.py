import myqueue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

binaryTree=TreeNode("drinks")
leftchild=TreeNode("hot")
rightchild=TreeNode("cold")
newchild=TreeNode("tea")
binaryTree.leftchild=leftchild
binaryTree.rightchild=rightchild
leftchild.leftchild=newchild

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customqueue = myqueue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
# levelorder(binaryTree)

def getdeepestNode(rootNode):
    if not rootNode:
        return "there is no rootnode or binary tree"
    else:
        customQueue= myqueue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
        deepNode=root.value
        return deepNode
# print(getdeepestNode(binaryTree).data)


def deletedeppestNOde(rootnode,node):
    if not rootnode:
        return "there is no rootnode or binary tree"
    else:
        customQueue= myqueue.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value is node:
                root.value=None
                return
            if root.value.rightchild :
                if root.value.rightchild is node:
                    root.value.rightchild =None
                    return
                else:
                    customQueue.enqueue(root.value.rightchild)
            if root.value.leftchild:
                if root.value.leftchild is node:
                    root.value.leftchild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftchild)

# new_node =getdeepestNode(binaryTree)
# deletedeppestNOde(binaryTree,new_node)
# levelorder(binaryTree)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = myqueue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getdeepestNode(rootNode)
                root.value.data = dNode.data
                deletedeppestNOde(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"
# deleteNodeBT(binaryTree,"drinks")
# levelorder(binaryTree)

def deleteBt(rootnode):
    rootnode.data=None
    rootnode.leftchild =None
    rootnode.righchilde=None

deleteBt(binaryTree)
levelorder(binaryTree)











