import myqueue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

binaryTree=TreeNode("drinks")
leftchild=TreeNode("hot")
rightchild=TreeNode("cold")
binaryTree.leftchild=leftchild
binaryTree.rightchild=rightchild

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

def binaryinsert(rootnode,new_nodevalue):
    if not rootnode:
        rootnode=new_nodevalue
    else:
        customQueue= myqueue.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=new_nodevalue
                return "successfully inserted"
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild=new_nodevalue
                return "successfully inserted"

new_node=TreeNode("tea")
print(binaryinsert(binaryTree,new_node))
levelorder(binaryTree)