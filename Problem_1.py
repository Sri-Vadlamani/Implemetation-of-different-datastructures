from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1


our_cache = LRUCache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 2);
our_cache.set(4, 3);
our_cache.set(5, 6);
print(our_cache.cache) #prints OrderedDict([(2, 2), (3, 2), (4, 3), (5, 6)])

print(our_cache.get(1))      # returns -1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(6, 6)
our_cache.set(7, 7)
print(our_cache.cache) #Prints OrderedDict([(5, 6), (2, 2), (6, 6), (7, 7)]) the cache reached it's capacity and eleminated 1,2,3

print(our_cache.get(6))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(1))        # returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(our_cache.get(None))  # returns -1
