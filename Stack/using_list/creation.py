class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()  # reverse without modifying original
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        self.list.append((value))
        return "the value is successfully appended"

    def pop(self):
        if self.list ==[]:
            return False
        else:
            self.list.pop()
            return "the value is successfully deleted"

    def peek(self):
        if self.list ==[]:
            return False
        else:
            return self.list[-1]

    def delete(self):
        self.list=[]

# Test
custom_stack = Stack()
# print(custom_stack.isEmpty())
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.pop()
# print(custom_stack.peek())
custom_stack.delete()
print(custom_stack)
