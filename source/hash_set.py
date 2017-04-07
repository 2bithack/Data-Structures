from hashtable import HashTable

class HashSet(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable()
        self.size = 0

    def contains(self, element):
        return self.hashtable.contains(element)

    def add(self, element):
        if not self.contains(element):
            self.hashtable.set(element, None)
            self.size += 1

    def remove(self, element):
        if self.contains(element):
            self.hashtable.delete(element)
            self.size -= 1

    def union(self, other_set):
        new_set = HashSet()
        for key in other_set.hashtable.keys():
            new_set.add(key)
        for key in self.hashtable.keys():
            new_set.add(key)
        return new_items

    def intersection(self, other_set):
        shared = HashSet()
        for key in other_set.hashtable.keys():
            if self.hashtable.contains(key) == True:
                shared.add(key)
        return shared

    def difference(self, other_set):
        different_items = HashSet()
        for key in other_set.hashtable.keys():
            if self.hashtable.contains(key) == False:
                different_items.add(key)
        for key in self.hashtable.keys():
            if other_set.hashtable.contains(key) == False:
                different_items.add(key)
        return different_items
        # different_items = []
        # for key in other_set.hashtable.keys():
        #     if self.contains(key) == False:
        #         new_items.append(key)
        # return new_items

    def is_subset(self, other_set):
        for key in other_set.hashtable.keys():
            if self.hashtable.contains(key) == False:
                return False
        return True
