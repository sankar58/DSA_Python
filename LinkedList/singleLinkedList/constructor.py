class Node:
    def __init__(self):
        self.value = None
        self.next=None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next

My_linked_list=SingleLinkedList()
print([temp.value for temp in My_linked_list])