# LINKED LIST STRUCTURE:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next

new_linked_list = LinkedList(7)
print("Head: ", new_linked_list.head.value)
print("Tail: ", new_linked_list.tail.value)
print("Linked List Size: ", new_linked_list.length)
print_list(new_linked_list)
# Prints the Linked List:

