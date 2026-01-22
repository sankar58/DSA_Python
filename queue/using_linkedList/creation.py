class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail=None

    def __iter__(self):
        temp =self.head
        while temp:
            yield temp
            temp=temp.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()

    def __str__(self):
        values=[str(x) for x in  self.linkedlist]
        return  " ".join(values)

    def enqueue(self,value):
        new_node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next=new_node
            self.linkedlist.tail=new_node
    def isEmpty(self):
        if self.linkedlist.head==None:
            return "the queue is empty"
    def dequeue(self):
        if self.isEmpty():
            "the queue is empty"
        else:
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head =self.linkedlist.head.next

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None


custom_queue=Queue()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
print(custom_queue.peek())
custom_queue.delete()
print(custom_queue)
