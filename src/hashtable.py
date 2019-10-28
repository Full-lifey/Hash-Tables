# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                current_pair.value = value
            else:
                if current_pair.next:
                    while current_pair.next:
                        current_pair == current_pair.next
                    else:
                        current_pair.next = LinkedPair(key, value)
                else:
                    current_pair.next = LinkedPair(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                print(current_pair.value)
                if current_pair.next:
                    self.storage[index] = current_pair.next
            elif current_pair.next:
                value = None
                while current_pair.next:
                    next = current_pair.next
                    if key == next.key:
                        value = next.value
                        current_pair.next = next.next
                    current_pair = current_pair.next
                else:
                    if value == None:
                        print("warning, key given is not in HashTable")
            else:
                print("warning, key given is not in HashTable")
        else:
            print("warning, key given is not in HashTable")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                return current_pair.value
            elif current_pair.next:
                value = None
                while current_pair.next:
                    if key == current_pair.next.key:
                        value = current_pair.next.value
                    current_pair = current_pair.next
                else:
                    return value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Double self.capacity
        self.capacity = self.capacity * 2
        # creates new storage of twice the size
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage
        for i in range(len(old_storage)):
            if old_storage[i] != None:
                if old_storage[i].next:
                    current = old_storage[i]
                    while current.next:
                        self.insert(current.key, current.value)
                        current = current.next
                    else:
                        self.insert(current.key, current.value)
                else:
                    self.insert(old_storage[i].key, old_storage[i].value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
