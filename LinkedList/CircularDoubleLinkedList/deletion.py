

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CirculardoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            if temp == self.head:
                break

    def creation(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        return "Circular doubly linked list created successfully"

    def insertion(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"

    def deletion(self,location):
        if self.head is None:
            print("the list list is empty")
        else:
            if location ==0:
                if self.head is None:
                    self.head.next =None
                    self.head.prev=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif location==1:
                    if self.head is None:
                        self.head.next = None
                        self.head.prev = None
                        self.head = None
                        self.tail = None
                    else:
                        self.tail=self.tail.prev
                        self.tail.next =self.head
                        self.head.prev= self.tail
            else:
                temp = self.head
                index=0
                while index <location-1:
                    temp=temp.next
                    index+=1
                temp.next= temp.next.next
                temp.next.prev=temp

my_circularL_linked_list = CirculardoubleLinkedList()
print(my_circularL_linked_list.creation(5))

my_circularL_linked_list.insertion(1,0)
my_circularL_linked_list.insertion(8,1)
my_circularL_linked_list.insertion(2,5)
my_circularL_linked_list.insertion(1,0)

my_circularL_linked_list.insertion(2,3)

my_circularL_linked_list.deletion(0)
my_circularL_linked_list.deletion(1)
my_circularL_linked_list.deletion(2)
# Print values in the circular doubly linked list
print([temp.value for temp in my_circularL_linked_list])

