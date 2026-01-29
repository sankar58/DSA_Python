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
    def levelorder(self,index):
        for i in range(index,self.lastUsedindex+1):
            print(self.list[i])

BTree= BinaryTree(6)
BTree.insert("drinks")
BTree.insert("hot")
BTree.insert("cold")
BTree.insert("tea")
BTree.insert("coffee")

BTree.levelorder(1)
