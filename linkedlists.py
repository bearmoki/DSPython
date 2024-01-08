
# Linked List:
# linked list has NO indexes 
# has a Head: (1st node)
# Tail: (last node)
# Will be spread out in spaces of memory

# Big O - Linked List

# ADDING TO THE TAIL:
# adding a node from the end of the list is O(1)
# removing a node from the end of the list is O(n) becuse would have to iterate over the head, each of the nodes to the very last node and set that last pointer to the last node (set tail)

# ADDING TO THE HEAD:
# Adding a node to the front of the list is O(1) - node points to the head - and head points to the new node
#  Removing the node, HEAD points to the existing node next, then that removes item from the linked list O(1)

# ADDING TO THE MIDDLE OF THE LIST:
# Iterate through the whole list to put that node in the middle - O(n)
# REMOVING TO THE MIDDLE OF THE LIST:
 # Iterate through the whole list to put that node in the middle - O(n)


# Node is not only the value but also the pointer
# Node is a dictionary

node = {
    "value": 4,
    "next": None
}

head = {
    "value": 11,
    "next":{
        "value": 23,
        "next": {
            "value": 7,
            "next": None
        }
    }
}

# print(head['next']['next']['value'])
# Can think of linked lists as nested dictionaries -
# each in different memory but can be accessed like nested dictionaries


# Linked List Constructor
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

    def append(self, value):
        new_node = Node(value)
        self.length +=1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def pop(self):
        # no items - head = none tail = none
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

# adding item to the beginning of the linkedlist
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            temp = new_node
            # new node points to head
            new_node.next = self.head
            # head points to new node
            self.head = new_node
        self.length += 1 
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            print(index)
            temp = temp.next
        return temp    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1 
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)    
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


        

    # def prepend(self, value):
    #     # create new node -> add node to beginning
    
    # def insert(self, index, value):
    #     # create new node -> insert node in specific index

my_linked_list = LinkedList(1)

my_linked_list.append(2)

# (2) Items - Return 2 Node
print(my_linked_list.pop())

# (2) Items - Return 1 Node
print(my_linked_list.pop())

# print(my_linked_list.insert(1,1))

# (2) Items - Return None
print(my_linked_list.pop())

# my_linked_list.print_list()


