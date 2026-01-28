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

    def searching(self,nodevalue):

        for i in range(len(self.list)):
            if self.list[i]==nodevalue:
                return "success"
        return "Not found"

BTree= BinaryTree(5)
print(BTree.insert("drinks"))
print(BTree.insert("hot"))
print(BTree.insert("cold"))
print(BTree.searching("cold"))
