#Create a class Node with instance variables data and next.
class Node:
    def __init__(self, data):
       self.value = data
       self.next = None

#Create a class LinkedList with instance variable head.
#Define methods get_prev_node, duplicate, append, remove.
class LinkedList:
    def __init__(self):
        self.head = None

#The method traverses the list from the first node and prints the data of each node.
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += " -> " + str(cur_head.value)
            cur_head = cur_head.next
        return out_string

#The method get_prev_node takes a reference node as argument and returns the previous node.
#It returns None when the reference node is the first node.
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

#The method append inserts a node at the last position of the list.
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

#The method remove takes a node as argument and removes it from the list.
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

#The method duplicate creates a copy of the list and returns it.
    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.value)
            copy.append(node)
            current = current.next
        return copy


#Define the function remove_duplicates which removes duplicate elements from the list passed as argument.
def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.value
        while current2:
            temp = current2
            current2 = current2.next
            if temp.value == data:
                llist.remove(temp)
        current1 = current1.next


#Define the function Union which returns the union of the two linked lists passed to it
def Union(llist1, llist2):
    if llist1.head is None:
        remove_duplicates(llist2)
        return llist2
    if llist2.head is None:
        remove_duplicates(llist1)
        return llist1


    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)

    return union


#Define the function Intersection which returns the intersection of the two linked lists passed to it.
def Intersection(llist_1, llist_2):
    if (llist_1.head is None or llist_2.head is None):
        return LinkedList()

    intersection = LinkedList()
    current1 = llist_1.head
    while current1:
        current2 = llist_2.head
        data = current1.value
        while current2:
            if current2.value == data:
                node = Node(data)
                intersection.append(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)

    return intersection


a_llist1 = LinkedList()
a_llist2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for data in element_1:
    node = Node(int(data))
    a_llist1.append(node)

for data in element_2:
    node = Node(int(data))
    a_llist2.append(node)
print("---------------test case-1-----------------------------------------------------------")
print("Union:",Union(a_llist1, a_llist2))
print("Intersection:",Intersection(a_llist1, a_llist2))

a_llist1 = LinkedList()
a_llist2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for data in element_1:
    node = Node(int(data))
    a_llist1.append(node)

for data in element_2:
    node = Node(int(data))
    a_llist2.append(node)
print("---------------test case-2-----------------------------------------------------------")
print("Union:",Union(a_llist1, a_llist2))
print("Intersection:",Intersection(a_llist1, a_llist2))

a_llist1 = LinkedList()
a_llist2 = LinkedList()
element_1 = []
element_2 = []

for data in element_1:
    node = Node(int(data))
    a_llist1.append(node)

for data in element_2:
    node = Node(int(data))
    a_llist2.append(node)
print("---------------test case-3-----------------------------------------------------------")
print("Union:",Union(a_llist1, a_llist2))
print("Intersection:",Intersection(a_llist1, a_llist2))

a_llist1 = LinkedList()
a_llist2 = LinkedList()
element_1 = [1,2,1,6,7,11,34]
element_2 = []

for data in element_1:
    node = Node(int(data))
    a_llist1.append(node)

for data in element_2:
    node = Node(int(data))
    a_llist2.append(node)
print("---------------test case-4-----------------------------------------------------------")
print("Union:",Union(a_llist1, a_llist2))
print("Intersection:",Intersection(a_llist1, a_llist2))

a_llist1 = LinkedList()
a_llist2 = LinkedList()
element_1 = []
element_2 = [1,2,1,6,7,11,34]

for data in element_1:
    node = Node(int(data))
    a_llist1.append(node)

for data in element_2:
    node = Node(int(data))
    a_llist2.append(node)
print("---------------test case-5-----------------------------------------------------------")
print("Union:",Union(a_llist1, a_llist2))
print("Intersection:",Intersection(a_llist1, a_llist2))
