### Description LRU:
A Least Recently Used (LRU) Cache organizes items in order of use, allowing to quickly identify which item hasn't been used for the longest amount of time

### Data structure:
An LRU cache is built by  OrderedDict data structure.
An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

### Implementation process:
The implementation is much cleaner as all the order bookkeeping is handled by the OrderDict now. For each get and set operation, first the item popped, then inserted back to update its timestamp. The element in the head of sequence is the least-used-item, thus the element to expire if the maximum capacity is reached.

### Time Complexity:
All of those steps are O(1), so put together it takes O(1) time to update cache each time an element is accessed

### Space Complexity:
 O(n), where n is the capacity of cache.

### References:
https://docs.python.org/2/library/collections.html#collections.OrderedDict
