### Description:
A function that provides an efficient look up of whether the user is in a group of Windows Active Directory.

### Implementation process & Data structure:
Traversing is done by walking through tree of users in the groups by defining a recursive function.
Returns true if the user is found else returns false

### Time Complexity:
Time complexity: O(nm) where n is the depth of the tree, m is number of users.

### Space Complexity:
Space complexity is O(nm). where n is the depth of the tree, m is number of users.
