class BinaryTree:
    def __init__(self,size):
        self.list=size*[None]
        self.lastUsedindex=0
        self.maxsize=size

    def insert(self,value):
        if self.lastUsedindex+1==self.maxsize:
            return "the binary treee is full"
        self.list[self.lastUsedindex+1]=value
        self.lastUsedindex +=1
        return "inserted successfully"

    def preorder(self,index):
        if index >self.lastUsedindex:
            return "index exceeded"
        print(self.list[index])
        self.preorder(index*2)
        self.preorder(index*2+1)
BTree= BinaryTree(5)
BTree.insert("drinks")
BTree.insert("hot")
BTree.insert("cold")
BTree.insert("tea")
BTree.insert("coffee")

BTree.preorder(1)


