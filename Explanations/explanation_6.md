### Description:
The program creates two linked lists and finds their union and intersection.

### Data structure:
* Single Linked lists

### Implementation process:
1. Created a class Node with instance variables data and next.
2. Created a class LinkedList with instance variable head.
3. The variable head points to the first element in the linked list.
4. Defined methods get_prev_node, duplicate, append, remove.
5. The method get_prev_node takes a reference node as argument and returns the previous node. It returns None when the reference node is the first node.
6. The method append inserts a node at the last position of the list.
7. The method remove takes a node as argument and removes it from the list.
8. The method duplicate creates a copy of the list and returns it.
9. Defined the function remove_duplicates which removes duplicate elements from the list passed as argument.
10. Defined the function Union which returns the union of the two linked lists passed to it.
11. Defined the function Intersection which returns the intersection of the two linked lists passed to it.
12. Prints the Union and Intersection of two linked lists

### Time Complexity:
1. Intersection of two linked lists: Overall time complexity is O(mn)
* 2 nested for loops are implemented. The outer loop is for each node of the 1st list and inner loop is for 2nd list. Each values in outer loop is compared with every value in inner loop to check if they are same. The time complexity of this method will be O(mn) where m and n are the numbers of nodes in two lists.
* Again remove_duplicate method is used to remove any duplicates in the final list which is O(n)

2. Union of two linked lists: Overall time complexity is O(n)
* The first list is traversed till the end and head of second list is made the next element of the end of first list. O(n)
* Again remove_duplicate method is used to remove any duplicates in the final list which is O(n)

### Space Complexity:
The space complexity for both union and intersection of linkedlists is O(n).
